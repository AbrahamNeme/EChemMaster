from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.views import APIView
from .serializers import CVEntrySerializer
from .services.cv_entry_service import CVEntryService

# Create your views here.
# request -> response
# request handler

# @method_decorator(csrf_exempt, name='dispatch')
# @permission_classes([AllowAny])


@api_view(['GET'])
def get_all_cventry(request):
    # Gets all existing entries in a form that can be serialized to JSON
    entries = CVEntryService. get_all_cventry()

    # Data is converted to JSON
    serializer = CVEntrySerializer(entries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cventry_by_material(request, material):
    # Finds and returns the entries with the matching material
    filtered_entries = CVEntryService.filter_cventry_by_electrode_material(material)
    print(filtered_entries)

    # Creates a list with the names of the matching entries
    entries_names = []
    for entry in filtered_entries:
        name = entry.package.resource_names[0]
        entries_names.append(name)
    print(entries_names)

    # Transforms the entries into a class that can be serialized to JSON
    entries = []
    for name in entries_names:
        cv = CVEntryService.get_cventry_by_name(name, True)
        entries.append(cv)

    # Data is converted to JSON
    serializer = CVEntrySerializer(entries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cventry_by_name(request, name):
    # Transforms the entries into a class that can be serialized to JSON
    cv_entry = CVEntryService.get_cventry_by_name(name, False)  # taguchi_2007_electrochemical_6023_f2b_solid

    # Data is converted to JSON
    serializer = CVEntrySerializer(cv_entry)
    return Response(serializer.data, status=status.HTTP_200_OK)
