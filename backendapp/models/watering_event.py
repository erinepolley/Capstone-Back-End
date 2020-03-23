from django.db import models
from .plant import Plant
from django.contrib.auth.models import User

class WateringEvent(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True, null=True)
    watered = models.BooleanField(default=True, null=True)    