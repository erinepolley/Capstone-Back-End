from django.shortcuts import redirect, render 
from django.urls import reverse
from backendapp.models import Plant
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def get_plant(plant_id):
    return Plant.objects.get(pk=plant_id)

@login_required
def plant_details(request, plant_id):
    if request.method == 'GET':
        plant = get_plant(plant_id)
        template_name = 'plant_detail.html'
        return render(request, template_name, {'plant': plant})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a plant
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            #retrieving the plant to update
            plant_to_update = Plant.objects.get(pk=plant_id)

             # Reassign a property's value
            plant_to_update.img_url = form_data['img_url']
            plant_to_update.name = form_data['name']
            plant_to_update.description = form_data['description']
            plant_to_update.day = form_data['day']
            plant_to_update.week = form_data['week']
            plant_to_update.type = form_data['plant_type']
            plant_to_update.notes = form_data['notes']
            # plant_to_update.reminder_time = form_data['reminder_time']
            # # Save the change to the db
            plant_to_update.save()

            return redirect(reverse('backendapp:plant'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):      
            plant = Plant.objects.get(pk=plant_id)
            plant.delete()

            return redirect(reverse('backendapp:home'))