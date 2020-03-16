from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backendapp.models import Plant
from .detail import get_plant


@login_required
def plant_form(request):
    if request.method == 'GET':
        plant_type_list = PlantType.objects.all()
        template = 'templates/plant_form.html'
        context = {
            'plant_types' = plant_type_list
        }
        return render(request, template, context)
      
@login_required
def plant_edit_form(request, plant_id):

    if request.method == 'GET':
        plant = get_plant(plant_id)

        template = 'templates/plant_form.html'
        context = {
            'plant': plant
        }

        return render(request, template, context)