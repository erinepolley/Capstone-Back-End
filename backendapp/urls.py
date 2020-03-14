from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', plant_list, name='home'),
    # path('plants/', plant_details, name='books'),
]