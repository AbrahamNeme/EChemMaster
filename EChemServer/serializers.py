from rest_framework import serializers
from .models import CVEntry


class CVEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CVEntry
        fields = '__all__'

