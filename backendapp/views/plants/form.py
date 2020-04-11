from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backendapp.models import Plant
from backendapp.models import PlantType
from .detail import get_plant


def get_plant_types():
    '''Returns all plant types from plant types table
'''
    return PlantType.objects.all()
#Getting the add a plant form
@login_required
def plant_form(request):
    '''Getting the form 
'''
    if request.method == 'GET':
        plant_type_list = get_plant_types()
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
        plant_type_list = get_plant_types()
        template = 'plant_form.html'
        context = {
            'plant': plant,
            'plant_types': plant_type_list
        }

        return render(request, template, context)