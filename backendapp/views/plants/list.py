from django.shortcuts import redirect, render, reverse
from backendapp.models import Plant
from django.contrib.auth.models import User
#It appears that details 
#This gets all the plants that the logged in user has added.

def plant_list(request):
    if request.method=='GET':
        current_user = User.objects.get(user=request.auth.user)
        user_plants = Plant.objects.filter(user=current_user)

        template = 'plants/list.html'
        context = {
                'user_plants': user_plants
        }

#Plant edit

#Plant delete
        return render(request, template, context)
