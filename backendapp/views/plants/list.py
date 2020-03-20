from django.shortcuts import redirect, render
from django.urls import reverse
from backendapp.models import Plant
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import pyautogui
from datetime import datetime, timezone
#This gets all the plants that the logged in user has added.
@login_required
def plant_list(request):
	if request.method=='GET':
		current_user = request.user
# def plant_water_time():
		dateTimeObj = datetime.now(timezone.utc)
		print("Today's full date time object", dateTimeObj)
		justTodaysDate=dateTimeObj.date()
		print("Just today's date", justTodaysDate)
		user_plants = Plant.objects.filter(user=current_user)
		for plant in user_plants:
			justPlantRemindDate = plant.reminder_time.date()
			print("Just the plant's reminder date", justPlantRemindDate)
			# if plant.reminder_time <= dateTimeObj:
			# 	pyautogui.confirm(text='f`{plant.name} the {plant.description} needs to be watered!`', title= 'Watering Time', buttons=['Water Now', 'Water Later'])
			# elif plant.time > dateTimeObj:
			# 	pyautogui.alert('Nothing to see here', 'Nothing')

		template = 'plant_list.html'
		context = {
			'user_plants': user_plants
		}
		return render(request, template, context)

	elif request.method == 'POST':
		form_data = request.POST
		current_user = request.user
		new_plant = Plant(
			user_id = current_user.id,
        	img_url = form_data['img_url'],
            name = form_data['name'],
            description = form_data['description'],
            days = form_data['days'],
            weeks = form_data['weeks'],
            plant_type_id = form_data['plant_type'],
            notes = form_data['notes']
		)
			#             plant_type_id = PlantType.objects.get(pk=form_data['plant_type']),
            #   reminder_time = form_data['reminder_time']
            # # Save the change to the db
		new_plant.save()
		return redirect(reverse('backendapp:home'))