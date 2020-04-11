from django.shortcuts import redirect, render
from django.urls import reverse
from backendapp.views.plants.detail import get_days_until_next_watering, check_form_data_days, check_form_data_weeks
from backendapp.models import Plant, WateringEvent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta

#This gets all the plants that the logged in user has added.
def returnAttributeValue(plant):
	'''Getting the daysTilWatering attribute. This way, I can sort the list of objects by the days until it's time to be watered.
	Argument: the plant object in the list being iterated over
'''
	return plant.daysTilWatering

@login_required
def plant_list(request):
	#Upon page load...
	if request.method=='GET':
		#Let's see who's logged in and store it in a variable.
		current_user = request.user
		user_plant_objects = Plant.objects.filter(user=current_user).order_by('-id')
		for plant in user_plant_objects:
			#Getting how many days until watering and then setting it as an attribute on each plant in user_plants. That way, I can pass it along to the template.
			daysTilWatering = get_days_until_next_watering(plant)
			setattr(plant, "daysTilWatering", daysTilWatering)
			# print("KEY VALUE IN PLANT", plant.daysTilWatering)
		#Sorting plants by days til watering	
		user_plants = sorted(user_plant_objects, key=returnAttributeValue)

		template = 'plant_list.html'
		context = {
			'user_plants': user_plants,
		}
		return render(request, template, context)

	elif request.method == 'POST':
		form_data = request.POST
        #When the user leaves days or weeks blank, the program throws an error. 
		#This is to set the value to 0 if the user leaves it blank without the error.
		days_value = check_form_data_days(form_data)
		weeks_value = check_form_data_weeks(form_data)

		current_user = request.user
		new_plant = Plant(
			user_id = current_user.id,
        	img_url = form_data['img_url'],
            name = form_data['name'],
            description = form_data['description'],
            days = days_value,
            weeks = weeks_value,
            plant_type_id = form_data['plant_type'],
            notes = form_data['notes'],
		)
            # Save the change to the db
		new_plant.save()
		return redirect(reverse('backendapp:plants'))