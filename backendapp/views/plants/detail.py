from django.shortcuts import redirect, render 
from django.urls import reverse
from backendapp.models import Plant, PlantType, WateringEvent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone, timedelta
#2020-03-19 23:18:27.162995

def get_plant(plant_id):
    return Plant.objects.get(pk=plant_id)

def get_plant_type(plant_type_id):
    return PlantType.objects.get(pk=plant_type_id)

@login_required
def plant_details(request, plant_id):
    if request.method == 'GET':
        plant = get_plant(plant_id)
        #Get last watering event.
        # beenWateredBool = WateringEvent.objects.get(plant_id=plant.id)
        # print(beenWateredBool)
        try:
            most_recent_watering_object = WateringEvent.objects.filter(plant_id=plant.id).order_by('-time')[0]
            # print('Most recent watering object', most_recent_watering_object)
        except:
            dateTimeObj = datetime.now(timezone.utc)
            justTodaysDate=dateTimeObj.date()
            dateThatPlantNeedsToBeWatered = justTodaysDate + timedelta(weeks=plant.weeks, days=plant.days)
            daysTilWatering = ((dateThatPlantNeedsToBeWatered - justTodaysDate).days)
        else:
            justPlantWateringDate = most_recent_watering_object.time.date()
            #Add plant.days/plant.weeks to it.
            dateThatPlantNeedsToBeWatered = justPlantWateringDate + timedelta(weeks=plant.weeks, days=plant.days)
            #Get today's date.
            dateTimeObj = datetime.now(timezone.utc)
            justTodaysDate=dateTimeObj.date()
            #Subtract today's date from date to be watered.
            #Store this value in a variable?
            daysTilWatering = ((dateThatPlantNeedsToBeWatered - justTodaysDate).days)

            # print('Days to next watering: %d' % ((dateThatPlantNeedsToBeWatered - justTodaysDate).days))
        print('Days Until Watering', daysTilWatering)
        #Sent it in context to 
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
        #When the user leaves days or weeks blank, the program throws an error. This is to set the value to 0 if the user leaves it blank without the error.
        if form_data['days']:
            days_value = form_data['days']
        else:
            days_value = 0

        if form_data['weeks']:
            weeks_value = form_data['weeks']
        else:
            weeks_value = 0

        # print('DAYS VALUE!', days_value)
        # print('WEEKS VALUE!', weeks_value)

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
            plant_to_update.days = days_value
            plant_to_update.weeks = weeks_value
            plant_to_update.plant_type_id = form_data['plant_type']
            plant_to_update.notes = form_data['notes']
            # plant_to_update.reminder_time = form_data['reminder_time']
            # # Save the change to the db
            plant_to_update.save()

            return redirect(reverse('backendapp:home'))

        # Check if this POST is for deleting a book
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):      
            plant = Plant.objects.get(pk=plant_id)
            plant.delete()
            return redirect(reverse('backendapp:home'))
  
        else:
            plant = get_plant(plant_id)
            current_user = request.user
            new_wateringevent = WateringEvent(
                plant_id = plant.id
            )
            new_wateringevent.save()
            return redirect(reverse('backendapp:watering'))

