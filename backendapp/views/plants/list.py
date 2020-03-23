from django.shortcuts import redirect, render
from django.urls import reverse
from backendapp.models import Plant, WateringEvent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone, timedelta

#This gets all the plants that the logged in user has added.
@login_required
def plant_list(request):
	#Upon page load...
	if request.method=='GET':
		#Let's see who's logged in and store it in a variable.
		current_user = request.user
		user_plants = Plant.objects.filter(user=current_user)
		print(user_plants)
		template = 'plant_list.html'
		context = {
			'user_plants': user_plants
		}
		return render(request, template, context)

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
            # # Save the change to the db
		new_plant.save()
		return redirect(reverse('backendapp:plants'))