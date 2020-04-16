import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''
    if request.method == "GET":
        template_name = 'registration/register.html'
        return render(request, template_name, {})
    # For handling when user submits the form data
    elif request.method == "POST":
        form_data = request.POST
        # password1 = form_data["password"]
        # password2 = form_data["password2"]
        # if password1 != password2:
        #     alert("Passwords need to match. ")
        new_user = User.objects.create_user(
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
        )

        authenticated_user = authenticate(
            email=form_data['email'],
            username=form_data['username'], 
            password=form_data['password']
        )

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return redirect(reverse('backendapp:home'))

        else:
            # Bad login details were provided. We need to let them know they need to fix this.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")        