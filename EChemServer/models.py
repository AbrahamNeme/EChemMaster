from django.db import models

# Create your models here.

class Electrode(models.Model):
    name = models.CharField(max_length=50)
    function = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    shape = models.CharField(max_length=50, blank=True, null=True)
    crystallographic_orientation = models.CharField(max_length=50, blank=True, null=True)
    preparation_procedure_description = models.TextField(blank=True, null=True)


# An Electrolyte is composed of one or many components
class ElectrolyteComponent(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    purity_grade = models.CharField(max_length=50, blank=True, null=True)
    total_ion_conductivity_value = models.FloatField(blank=True, null=True)
    total_ion_conductivity_unit = models.CharField(max_length=10, null=True, blank=True)


class Electrolyte(models.Model):
    type = models.CharField(max_length=50)
    components = models.JSONField()


class CVEntry(models.Model):
    name = models.CharField(max_length=100)
    t = models.JSONField()
    t_unit = models.CharField(max_length=20)
    E = models.JSONField()
    E_unit = models.CharField(max_length=20)
    j = models.JSONField()
    j_unit = models.CharField(max_length=20)
    scanrate_value = models.JSONField()
    scanrate_unit = models.CharField(max_length=20)
    we_electrode = models.JSONField()
    ref_electrode = models.JSONField()
    ce_electrode = models.JSONField()
    electrolyte = models.JSONField()
    source = models.JSONField()
    citation = models.CharField(max_length=500)
    bibliography = models.JSONField()
