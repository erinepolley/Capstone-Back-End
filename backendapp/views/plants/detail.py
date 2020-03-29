from django.shortcuts import redirect, render 
from django.urls import reverse
from backendapp.models import Plant, PlantType, WateringEvent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.http import HttpResponseRedirect


def get_plant(plant_id):
    '''Returns all plants belonging to the authenticated user 
    Arguments: Plant id passed through URL
'''
    return Plant.objects.get(pk=plant_id)

def get_plant_type(plant_type_id):
    '''Returns the plant type of the plant
'''
    return PlantType.objects.get(pk=plant_type_id)

def get_days_until_next_watering(plant_object):
    '''Returns how many days left until the plant needs water
'''
    #Get today's date.
    justTodaysDate=date.today()
    try:
        most_recent_watering_object = WateringEvent.objects.filter(plant_id=plant_object.id).order_by('-time')[0]
        # print('Most recent watering object', most_recent_watering_object)
    except:
        dateThatPlantNeedsToBeWatered = justTodaysDate + timedelta(weeks=plant_object.weeks, days=plant_object.days)
        daysTilWatering = ((dateThatPlantNeedsToBeWatered - justTodaysDate).days)
    else:
        justPlantWateringDate = most_recent_watering_object.time
        #Add plant.days/plant.weeks to it.
        dateThatPlantNeedsToBeWatered = justPlantWateringDate + timedelta(weeks=plant_object.weeks, days=plant_object.days)
        #Subtract today's date from date to be watered.
        daysTilWatering = ((dateThatPlantNeedsToBeWatered - justTodaysDate).days)
    # print('Days Until Watering', daysTilWatering)
    return daysTilWatering

@login_required
def plant_details(request, plant_id):
    if request.method == 'GET':
        plant = get_plant(plant_id)
        daysTilWatering = get_days_until_next_watering(plant)

        #Sent it in context to the template
        plant_type = get_plant_type(plant.plant_type_id)
        template_name = 'plant_detail.html'
        context = {
            'plant': plant,
            'plant_type': plant_type,
            'days_til_watering': daysTilWatering
        }
        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST
        plant_to_update = get_plant(plant_id)
        # Check if this POST is for editing a plant
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
        #When the user leaves days or weeks blank, the program throws an error. This is to set the value to 0 if the user leaves it blank without the error.
            if form_data['days']:
                days_value = form_data['days']
            else:
                days_value = 0

            if form_data['weeks']:
                weeks_value = form_data['weeks']
            else:
                weeks_value = 0
                
            if form_data['img_url']:
                picture = form_data['img_url']
            else:
                picture = plant_to_update.img_url
            print(picture)
            #retrieving the plant to update

             # Reassign a property's value
            plant_to_update.img_url = picture
            plant_to_update.name = form_data['name']
            plant_to_update.description = form_data['description']
            plant_to_update.days = days_value
            plant_to_update.weeks = weeks_value
            plant_to_update.plant_type_id = form_data['plant_type']
            plant_to_update.notes = form_data['notes']

            # # Save the change to the db
            plant_to_update.save()

            # go back to details view so you can see your changes
            return HttpResponseRedirect(request.path_info)

        # Check if POST is really deleting a plant
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):      
            plant = get_plant(plant_id)
            plant.delete()
            return redirect(reverse('backendapp:plants'))

        else:
            plant = get_plant(plant_id)
            new_wateringevent = WateringEvent(
                plant_id = plant.id
            )
            new_wateringevent.save()
            return redirect(reverse('backendapp:home'))

