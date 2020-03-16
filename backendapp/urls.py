from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', plant_list, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('plants/<int:plant_id>', plant_details, name='plant'),
]