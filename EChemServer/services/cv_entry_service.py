from unitpackage.cv.cv_collection import CVCollection
from EChemServer.models import CVEntry


class CVEntryService:

    db = CVCollection()

    @classmethod
    def get_all_cventry(cls):
        all_entries = []
        for entry in cls.db:
            all_entries.append(cls.get_cventry_by_name(entry.package.resource_names[0], True))
        return all_entries

    @classmethod
    def get_cventry_by_name(cls, name, is_many):
        db_entry = cls.db[name]

        entry = CVEntry()
        entry.name = name

        if not is_many:
            columns_as_lists = db_entry.df.values.T.tolist()
            entry.t = columns_as_lists[0]
            entry.t_unit = db_entry.field_unit('t')
            entry.E = columns_as_lists[1]
            entry.E_unit = db_entry.field_unit('E')
            entry.j = columns_as_lists[2]
            entry.j_unit = db_entry.field_unit('j')

        entry.electrolyte = db_entry.system.electrolyte.__dict__
        if cls.is_electrode_present('WE', db_entry.system.electrodes):
            entry.we_electrode = db_entry.get_electrode('WE').__dict__
        if cls.is_electrode_present('REF', db_entry.system.electrodes):
            entry.ref_electrode = db_entry.get_electrode('REF').__dict__
        if cls.is_electrode_present('CE', db_entry.system.electrodes):
            entry.ce_electrode = db_entry.get_electrode('CE').__dict__

        entry.source = db_entry.source.__dict__
        entry.citation = db_entry.citation(backend='text')

        bib = dict()
        bib['type'] = db_entry.bibliography.__dict__['type']
        bib['title'] = db_entry.bibliography.fields['title']
        if 'journal' in db_entry.bibliography.fields:
            bib['journal'] = db_entry.bibliography.fields['journal']
        if 'volume' in db_entry.bibliography.fields:
            bib['volume'] = db_entry.bibliography.fields['volume']
        if 'number' in db_entry.bibliography.fields:
            bib['number'] = db_entry.bibliography.fields['number']
        if 'pages' in db_entry.bibliography.fields:
            bib['pages'] = db_entry.bibliography.fields['pages']
        if 'year' in db_entry.bibliography.fields:
            bib['year'] = db_entry.bibliography.fields['year']
        if 'publisher' in db_entry.bibliography.fields:
            bib['publisher'] = db_entry.bibliography.fields['publisher']
        authors = []
        for author in db_entry.bibliography.persons['author']:
            if len(author.last_names) > 0 and len(author.first_names) > 0:
                authors.append(f'{author.last_names[0]}, {author.first_names[0]}')
            elif len(author.last_names) > 0 == len(author.first_names):
                authors.append(f'{author.last_names[0]}')
        bib['authors'] = authors
        entry.bibliography = bib

        return entry

    @classmethod
    def is_electrode_present(cls, electrode_name, electrodes):
        names = []
        for electrode in electrodes:
            names.append(electrode['name'])

        is_present = False
        for name in names:
            if name == electrode_name:
                is_present = True
        return is_present

    @classmethod
    def has_material(cls, entry, material):
        electrode = entry.get_electrode('WE')
        return electrode and electrode['material'] == material

    @classmethod
    def filter_cventry_by_electrode_material(cls, material):
        entries = [entry for entry in cls.db if cls.has_material(entry, material)]
        return entries
