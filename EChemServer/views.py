from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from unitpackage.cv.cv_entry import CVEntry as Entry
from .serializers import CVEntrySerializer
from unitpackage.cv.cv_collection import CVCollection
import json
from .models import CVEntry, Electrolyte, ElectrolyteComponent
from .services.cvEntryService import CVEntryService

# Create your views here.


@api_view(['GET'])
def get_all_cventry(request):
    db = CVCollection()
    json_data = db['briega_martos_2018_understanding_j3045_p1_f1d_black']
    electrolyte = json_data.system.electrolyte
    #print(json_data)
    #json_data = [entry.__dict__ for entry in db]

    entries = db.filter(lambda entry: entry.get_electrode('WE').material == 'Pt')
    print(entries)
    return Response(electrolyte.__dict__, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cventry_by_name(request):
    db = CVCollection()
    db_entry = db['taguchi_2007_electrochemical_6023_f2b_solid']
    cv_entry = CVEntry()
    cv_entry.name = 'taguchi_2007_electrochemical_6023_f2b_solid'
    columns_as_lists = db_entry.df.values.T.tolist()
    cv_entry.t = columns_as_lists[0]
    cv_entry.E = columns_as_lists[1]
    cv_entry.j = columns_as_lists[2]
    print(db_entry.system.electrolyte)

    # Create Electrolyte instance
    electrolyte = Electrolyte()
    electrolyte.type = db_entry.system.electrolyte['type']
    electrolyte.save()
    # Create ElectrolyteComponent instances and add them to the Electrolyte
    for component_data in db_entry.system.electrolyte['components']:
        component = ElectrolyteComponent(
            name=component_data['name'],
            type=component_data['type'],
            source=component_data['source'],
        )
        if 'purity' in component_data:
            component.purity_grade = component_data['purity']['grade']
            component.total_ion_conductivity_value = component_data['purity']['total ion conductivity']['value']
            component.total_ion_conductivity_unit = component_data['purity']['total ion conductivity']['unit']
        else:
            component.purity_grade = " "
            component.total_ion_conductivity_value = 0.0
            component.total_ion_conductivity_unit = " "
        component.save()
        electrolyte.components.add(component)
    cv_entry.electrolyte = electrolyte
    serializer = CVEntrySerializer(cv_entry)
    return Response(serializer.data, status=status.HTTP_200_OK)
