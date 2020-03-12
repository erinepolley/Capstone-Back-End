from django.db import models
from django.contrib.auth.models import User
class Plant(models.Model):
#user, type, name, description, img_url, day, week, notes, reminder_time
    user = models.CharField(max_length=100)
    plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    days = models.IntegerField()
    weeks = models.IntegerField()
    notes = models.CharField(max_length=200)
    reminder_time = models.DateField(null=True, blank=True, default=None)
