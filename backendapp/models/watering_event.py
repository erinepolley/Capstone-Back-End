from django.db import models
from .plant import Plant
from django.contrib.auth.models import User

class WateringEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, null=True)    
    watered = models.BooleanField(default=False)