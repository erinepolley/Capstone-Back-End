from django.shortcuts import redirect, render, reverse
from backendapp.models import Plant
from django.contrib.auth.models import User

def get_plant(plant_id):
    return plant.objects.get(pk=plant_id)


# @login_required
def plant_details(request, plant_id):
    if request.method == 'GET':
        plant = get_plant(plant_id)
        template_name = 'detail.html'
        return render(request, template_name, {'plant': plant})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a plant
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"

            plant_to_update = Plant.objects.get(pk=plant_id)

            # # Reassign a property's value
            plant_to_update.title = form_data['title']
            plant_to_update.author = form_data['author']
            plant_to_update.isbn = form_data['isbn']
            plant_to_update.year = form_data['year_published']
            plant_to_update.location_id = form_data['location']

            # # Save the change to the db
            plant_to_update.save()

            return redirect(reverse('backendapp:home'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #         DELETE FROM libraryapp_book
            #         WHERE id = ?
            #     """, (book_id,))
                
            plant = Plant.objects.get(pk=plant_id)
            plant.delete()

            return redirect(reverse('backendapp:home'))