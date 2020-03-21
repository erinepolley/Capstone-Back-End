# from models.plant import Plant
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect, render
# from django.urls import reverse
# from datetime import datetime, timedelta
# from views.plants.detail import get_plant


# @login_required
# def plant_water():
#     #THIS EVENT IS A POST. Instantiating a new Watering Event and saving it to the db.
#     # plant = get_plant(plant_id)
# 	# new_wateringevent = WateringEvent(
#     #     plant = plant
# 	# )
# 	# new_wateringevent.save()
#     #THIS EVENT IS A PUT. Modifying two fields in this plant object and saving it to the db. 
#     new_reminder_time = datetime.now() + timedelta(days=plant.days, weeks=plant.weeks)
#     print(new_reminder_time)
#     plant.img_url = plant.img_url,
#     plant.name = plant.name,
#     plant.description = plant.description,
#     plant.days = plant.days,
#     plant.weeks = plant.weeks,
#     plant.plant_type_id = plant.plant_type_id,
#     plant.notes = plant.notes,
#     plant.reminder_time = new_reminder_time
#     plant.watered = True
#     # Save the change to the db
#     plant_to_update.save()
#     return redirect(reverse('backendapp:home'))