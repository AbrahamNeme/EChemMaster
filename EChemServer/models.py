from django.db import models

# Create your models here.


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
