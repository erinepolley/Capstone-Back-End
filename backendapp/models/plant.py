from django.db import models
from django.contrib.auth.models import User
from .plant_type import PlantType

class Plant(models.Model):
#user, type, name, description, img_url, day, week, notes, reminder_time
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    days = models.IntegerField(default=0, null=True, blank=True)
    weeks = models.IntegerField(default=0, null=True, blank=True)
    notes = models.CharField(max_length=200)
    reminder_time = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
