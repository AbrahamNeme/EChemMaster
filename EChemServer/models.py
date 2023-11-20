from django.db import models
import json

# Create your models here.


class Electrode(models.Model):
    name = models.CharField(max_length=50)
    function = models.CharField(max_length=50)
    type = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=50, blank=True, null=True)
    shape = models.CharField(max_length=50, blank=True, null=True)
    crystallographic_orientation = models.CharField(max_length=50, blank=True, null=True)
    preparation_procedure_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.function}"


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
    components = models.ManyToManyField(ElectrolyteComponent, null=True)

    def create_electrolyte(data):
        # Create Electrolyte instance
        electrolyte = Electrolyte(type=data['type'])

        # Create ElectrolyteComponent instances and add them to the Electrolyte
        #components_list = []
        for component_data in data['components']:
            component = ElectrolyteComponent(
                name=component_data['name'],
                type=component_data['type'],
                source=component_data['source'],
            )
            # Check if 'purity' key exists before accessing its values
            try:
                component.purity_grade = component_data['purity']['grade']
                component.total_ion_conductivity_value = component_data['purity']['total ion conductivity']['value']
                component.total_ion_conductivity_unit = component_data['purity']['total ion conductivity']['unit']
            except KeyError as e:
                print(f"KeyError: {e}")

            #components_list.append(component)

            # Serialize the list of components and assign it to the JSONField
            electrolyte.components.add(component)
            #electrolyte.components = [comp.__dict__ for comp in components_list]

        return electrolyte


class CVEntry(models.Model):
    name = models.CharField(max_length=100)
    t = models.JSONField()
    E = models.JSONField()
    j = models.JSONField()
    electrodes = models.ManyToManyField(Electrode, null=True)
    electrolyte = models.ForeignKey(Electrolyte, on_delete=models.SET_NULL, null=True)
