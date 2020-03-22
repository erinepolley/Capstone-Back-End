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
		# print('FORM DATA WEEKS', form_data['weeks'])
		# print('FORM DATA DAYS', form_data['days'])
		# reminder_time = datetime.now() + timedelta(weeks=form_data['weeks'], days=form_data['days'])
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
			# reminder_time = reminder_time
		)
            # # Save the change to the db
		new_plant.save()
		return redirect(reverse('backendapp:home'))