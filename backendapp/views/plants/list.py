from django.shortcuts import redirect, render
from django.urls import reverse
from backendapp.models import Plant
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#This gets all the plants that the logged in user has added.
@login_required
def plant_list(request):
	if request.method=='GET':
		current_user = request.user
        #current_user = User.objects.get(user=request.user)
		user_plants = Plant.objects.filter(user=current_user)
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