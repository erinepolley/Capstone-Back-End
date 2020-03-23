from django.shortcuts import redirect, render
from django.urls import reverse
from backendapp.models import Plant, WateringEvent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date, timezone, timedelta

@login_required
def watering_list(request):
	#Upon page load...
	if request.method=='GET':
		#Let's see who's logged in and store it in a variable.
		current_user = request.user
		#What is today's date?
		justTodaysDate=date.today()
		print("Just today's date", justTodaysDate)
		#Let's get all the plants for this user.
		user_plants = Plant.objects.filter(user=current_user)
		#Empty array to store all the plants that need to be watered. To be explained below...
		listOfThirstyPlants = []
		#NOW for each of the user's plants...
		for plant in user_plants:
			try:
			#... we need to get the most recent watering date for that plant. This involves getting all the watering events of the plant, ordering them by most recent, and grabbing the most recent one off the top. 
				most_recent_watering_object = WateringEvent.objects.filter(plant_id=plant.id).order_by('-time')[0]
				# print("MOST RECENT WATERING", most_recent_watering_object)
				#Then, let's isolate the date of the most recent watering from the datetime.
				justPlantWateringDate = most_recent_watering_object.time
				# print("Most recent watering", justPlantWateringDate)
				#Doing some simple math to determine the date that the plant needs to be watered.
				dateThatPlantNeedsToBeWatered = justPlantWateringDate + timedelta(weeks=plant.weeks, days=plant.days)
				# print("dateThatPlantNeedsToBeWatered", dateThatPlantNeedsToBeWatered)
			except:
				dateThatPlantNeedsToBeWatered = justTodaysDate + timedelta(weeks=plant.weeks, days=plant.days)		
			#If today's date is past the date that the plant needs to be watered, add the plant to the thirsty plant list.
			if dateThatPlantNeedsToBeWatered <= justTodaysDate:
				listOfThirstyPlants.append(plant)
				# print(listOfThirstyPlants)
				print(f'{plant.name} the {plant.description} needs to be watered!')
			else:
				print(f'{plant.name} the {plant.description} is fine.')
		#Let's send these thirsty plants to a template to let the user know!
		template = 'plant_watering.html'
		context = {
			'thirsty_plants': listOfThirstyPlants,
			'current_user': current_user
		}
		return render(request, template, context)