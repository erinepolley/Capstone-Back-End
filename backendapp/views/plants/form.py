from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from backendapp.models import Plant
from .detail import get_plant


@login_required
def plant_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'templates/form.html'


        return render(request, template)
      
@login_required
def plant_edit_form(request, plant_id):

    if request.method == 'GET':
        plant = get_plant(plant_id)

        template = 'templates/form.html'
        context = {
            'plant': plant
        }

        return render(request, template, context)