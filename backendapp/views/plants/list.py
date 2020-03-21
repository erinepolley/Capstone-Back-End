from django.shortcuts import redirect, render
from django.urls import reverse
from backendapp.models import Plant, WateringEvent
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# import pyautogui
from datetime import datetime, timezone, timedelta
import schedule
#This gets all the plants that the logged in user has added.

@login_required
def plant_list(request):
	#Upon page load...
	if request.method=='GET':
		#Let's see who's logged in and store it in a variable.
		current_user = request.user
		#What is today's date? Let's 1) make a datetime object and 2) extract it from there.
		dateTimeObj = datetime.now(timezone.utc)
		print("Today's full date time object", dateTimeObj)
		justTodaysDate=dateTimeObj.date()
		print("Just today's date", justTodaysDate)
		#Let's get all the plants for this user.
		user_plants = Plant.objects.filter(user=current_user)
		#NOW for each of the user's plants...
		for plant in user_plants:
			#... we need to get the most recent watering date for that plant. This involves getting all the watering events of the plant, ordering them by most recent, and grabbing the most recent one off the top. 
			most_recent_watering_object = WateringEvent.objects.filter(plant_id=plant.id).order_by('-time')[0]
			# print("MOST RECENT WATERING", most_recent_watering_object)
			#Then, let's isolate the date of the most recent watering.
			justPlantWateringDate = most_recent_watering_object.time.date() 
			# print("Just the plant's reminder date?", justPlantWateringDate)
			dateThatPlantNeedsToBeWatered = justPlantWateringDate + timedelta(weeks=plant.weeks, days=plant.days)
			# print("dateThatPlantNeedsToBeWatered", dateThatPlantNeedsToBeWatered)
			if dateThatPlantNeedsToBeWatered <= justTodaysDate:
				print(f'{plant.name} the {plant.description} needs to be watered!')
			else:
				print(f'{plant.name} the {plant.description} is fine.')



			# difference_in_dates_integer = justTodaysDate - justPlantRemindDate 
			# print("TIME DELTA", difference_in_dates_integer)
			# if total_time < difference_in_dates_integer:
			# 	 pyautogui.confirm(text=f'{plant.name} the {plant.description} needs to be watered!', title= 'Watering Time', buttons=['Water Now', 'Water Later'])
			# else:
			# 	pyautogui.confirm(text=f'{plant.name} the {plant.description} is fine.', title= 'Watering Time', buttons='Cool')	



		template = 'plant_list.html'
		context = {
			'user_plants': user_plants
		}
		return render(request, template, context)

	elif request.method == 'POST':
		form_data = request.POST
		print('FORM DATA WEEKS', form_data['weeks'])
		print('FORM DATA DAYS', form_data['days'])
		reminder_time = datetime.now() + timedelta(weeks=form_data['weeks'], days=form_data['days'])
		current_user = request.user
		new_plant = Plant(
			user_id = current_user.id,
        	img_url = form_data['img_url'],
            name = form_data['name'],
            description = form_data['description'],
            days = form_data['days'],
            weeks = form_data['weeks'],
            plant_type_id = form_data['plant_type'],
            notes = form_data['notes'],
			reminder_time = reminder_time
		)
            # # Save the change to the db
		new_plant.save()
		return redirect(reverse('backendapp:home'))