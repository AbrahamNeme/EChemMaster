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

        entry.electrolyte = db_entry.system.electrolyte.__dict__['_descriptor']

        if cls.is_electrode_present('WE', db_entry.system.electrodes):
            entry.we_electrode = cls.create_we_electrode(db_entry.get_electrode('WE').__dict__['_descriptor'])

        if cls.is_electrode_present('REF', db_entry.system.electrodes):
            entry.ref_electrode = cls.create_ref_electrode(db_entry.get_electrode('REF').__dict__['_descriptor'])

        if cls.is_electrode_present('CE', db_entry.system.electrodes):
            entry.ce_electrode = cls.create_ce_electrode(db_entry.get_electrode('CE').__dict__['_descriptor'])

        entry.source = db_entry.source.__dict__
        entry.citation = db_entry.citation(backend='text')

        entry.bibliography = cls.create_bibliography(db_entry.bibliography)

        return entry

    @classmethod
    def create_ce_electrode(cls, ce):
        ce_electrode = dict()
        ce_electrode['name'] = ce['name']
        ce_electrode['function'] = ce['function']
        ce_electrode['material'] = ce['material']
        if 'crystallographic orientation' in ce:
            ce_electrode['crystallographicOrientation'] = ce['crystallographic orientation']
        if 'supplier' in ce:
            ce_electrode['supplier'] = ce['supplier']
        if 'shape' in ce:
            ce_electrode['shape'] = ce['shape']
        return ce_electrode

    @classmethod
    def create_ref_electrode(cls, ref):
        ref_electrode = dict()
        ref_electrode['name'] = ref['name']
        ref_electrode['function'] = ref['function']
        if 'source' in ref:
            if 'supplier' in ref['source']:
                ref_electrode['source'] = ref['source']['supplier']
            else:
                ref_electrode['source'] = ref['source']
        if 'supplier' in ref:
            ref_electrode['supplier'] = ref['supplier']
        if 'type' in ref:
            ref_electrode['type'] = ref['type']
        return ref_electrode

    @classmethod
    def create_we_electrode(cls, we):
        we_electrode = dict()
        we_electrode['name'] = we['name']
        we_electrode['function'] = we['function']
        we_electrode['material'] = we['material']
        we_electrode['crystallographicOrientation'] = we['crystallographic orientation']
        if 'geometric electrolyte contact area' in we:
            we_electrode['geometricElectrolyteContactArea'] = we['geometric electrolyte contact area']['unit']
        if 'shape' in we:
            we_electrode['shape'] = we['shape']
        if 'source' in we:
            we_electrode['source'] = we['source']
        return we_electrode

    @classmethod
    def create_bibliography(cls, bibliography):
        bib = dict()
        bib['type'] = bibliography.__dict__['type']
        bib['title'] = bibliography.fields['title']
        if 'journal' in bibliography.fields:
            bib['journal'] = bibliography.fields['journal']
        if 'volume' in bibliography.fields:
            bib['volume'] = bibliography.fields['volume']
        if 'number' in bibliography.fields:
            bib['number'] = bibliography.fields['number']
        if 'pages' in bibliography.fields:
            bib['pages'] = bibliography.fields['pages']
        if 'year' in bibliography.fields:
            bib['year'] = bibliography.fields['year']
        if 'publisher' in bibliography.fields:
            bib['publisher'] = bibliography.fields['publisher']
        authors = []
        for author in bibliography.persons['author']:
            if len(author.last_names) > 0 and len(author.first_names) > 0:
                authors.append(f'{author.last_names[0]}, {author.first_names[0]}')
            elif len(author.last_names) > 0 == len(author.first_names):
                authors.append(f'{author.last_names[0]}')
        bib['authors'] = authors
        return bib

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
