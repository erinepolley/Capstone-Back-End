from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User

def register_user(request):
    """View method for handling creation of a new user for auth
        Args:
        request = full http object
    """

    # For handling when user submits the form data
    if request.method == "POST":

        # First create a new user using django's built in craziness. create_user is a method in django.
        new_user = User.objects.create_user(
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
        )

        login(request, new_user)

        # Redirect the browser to wherever you want to go after registering
        return redirect(reverse('backendapp:home'))

    # handles a request to load the empty form for the user to fill out
    else:
        template = 'registration/register.html'

    return render(request, template, {})