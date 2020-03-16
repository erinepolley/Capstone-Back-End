from django.urls import include, path
from .views import *

app_name = "backendapp"

urlpatterns = [
    path('', plant_list, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('plants/<int:plant_id>', plant_details, name='plant'),
    path('plant/form', plant_form, name='plant_form'),
    path('plants/<int:plant_id>/form/', plant_edit_form, name='plant_edit_form'),

]