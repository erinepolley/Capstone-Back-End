from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backendapp.models import Plant
from backendapp.models import PlantType
from .detail import get_plant

#Getting the add a plant form
@login_required
def plant_form(request):
    if request.method == 'GET':
        plant_type_list = PlantType.objects.all()
        template = 'plant_form.html'
        context = {
            'plant_types': plant_type_list
        }
        return render(request, template, context)

#Getting the plant edit form
@login_required
def plant_edit_form(request, plant_id):
    if request.method == 'GET':
        plant = get_plant(plant_id)
        # print(plant.notes)
        plant_type_list = PlantType.objects.all()
        template = 'plant_form.html'
        context = {
            'plant': plant,
            'plant_types': plant_type_list
        }

        return render(request, template, context)