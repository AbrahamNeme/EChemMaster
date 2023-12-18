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
    def get_cventry_by_name(cls, name, skip_plot_data):
        db_entry = cls.db[name]

        entry = CVEntry()
        entry.name = name

        if not skip_plot_data:
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

        entry.source = cls.create_source(db_entry.source.__dict__['_descriptor'])
        #entry.source = db_entry.source.__dict__['_descriptor']
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
    def create_source(cls, so):
        source = dict()
        source['citationKey'] = so['citation key']
        source['url'] = so['url']
        if 'techniques' in so:
            if isinstance(so['techniques'], list):
                source['techniques'] = so['techniques']
            else:
                source['techniques'] = so['techniques'].split(", ")
        source['figure'] = so['figure']
        source['curve'] = so['curve']
        source['bibdata'] = so['bibdata']
        return source

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

    @classmethod
    def normalize_ref(cls, entry, ref_electrode):
        try:
            entry_ref_potential = entry.get_electrode('REF')['potential']
        except:
            entry_ref_potential = 4.44

        refs = {
             'Ag/AgCl': 4.637,
             'Ag/AgCl-sat': 4.637,
             'Ag/AgCl_3M': 4.637,
             'Hg/HgO/0.1 M NaOH': 4.9,  ### Dummy data
             'RHE': 4.44,  ### Dummy Data
             'SCE': 4.688,
             'wire': 5.55, ### Dummy Data,
             'SHE': 4.44,
             'NCE': 4.720
        }
        if ref_electrode not in refs:
            raise ValueError(f"Unknown reference electrode type: {ref_electrode}")

        return entry_ref_potential - refs[ref_electrode]



    @classmethod
    def normalize_cyclic_voltammogram(cls,entry, reference_electrode=None):

        try:
            # If reference_electrode is not provided, use 'SHE' as the default
            if reference_electrode is None:
                reference_electrode = 'SHE'

            # Check if the necessary keys are present in the CV entry
            if 'system' in entry and 'electrodes' in entry['system']:

                # Find the reference electrode in the list of electrodes
                ref_electrode_data = next(
                    (electrode for electrode in entry.system.electrodes if electrode['name'] == reference_electrode),
                    None
                )

                # Check if the reference electrode was found
                if ref_electrode_data is None:
                    raise ValueError(f"Reference electrode '{reference_electrode}' not found in the entry.")
            else:
                # 'system' or 'electrodes' key not found
                raise ValueError("Invalid CV entry structure.")

            # Get the potential of the reference electrode for normalization
            ref_potential = cls.normalize_ref(entry, reference_electrode)

            # Normalize the potential values
            normalized_potentials = [potential - ref_potential for potential in
                                     entry['package']['resources'][0]['data']['E']]

            # Create a new CVEntry instance with normalized data
            normalized_entry = CVEntry(
                    name=entry['package']['resources'][0]['name'],
                    t=entry['package']['resources'][0]['data']['t'],
                    t_unit=entry['package']['resources'][0]['data']['t_unit'],
                    E=normalized_potentials,
                    E_unit=entry['package']['resources'][0]['data']['E_unit'],
                    j=entry['package']['resources'][0]['data']['j'],
                    j_unit=entry['package']['resources'][0]['data']['j_unit'],
                    we_electrode=None,  # Update with the actual working electrode name
                    ref_electrode=reference_electrode,
                    ce_electrode=None,  # Update with the actual counter electrode name
                    electrolyte=entry['system']['electrolyte'],
                    source=entry['source'],
                    citation=entry['source']['citation key'],
                    bibliography=entry['source']['bibdata']
            )

            return normalized_entry

        except Exception as e:
            # Handle exceptions
            print(f"Error in normalize_cyclic_voltammogram: {e}")

            return None
