from django.shortcuts import redirect, render, reverse
from backendapp.models import Plant
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#This gets all the plants that the logged in user has added.
@login_required
def plant_list(request):
    if request.method=='GET':
        current_user = request.user
        # current_user = User.objects.get(user=request.user)
        user_plants = Plant.objects.filter(user=current_user)

        

        template = 'plant_list.html'
        context = {
                'user_plants': user_plants
        }


        return render(request, template, context)
