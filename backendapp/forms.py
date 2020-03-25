from django.forms import ModelForm
from .models.plant import Plant

class AddPlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['plant_type', 'name', 'img_url', 'days', 'weeks', 'notes']
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # plant_type = models.ForeignKey(PlantType, on_delete=models.CASCADE, null=True)
    # name = models.CharField(max_length=50)
    # description = models.CharField(max_length=200)
    # img_url = models.ImageField(upload_to='media', blank=True)
    # days = models.IntegerField(default=0, null=True, blank=True)
    # weeks = models.IntegerField(default=0, null=True, blank=True)
    # notes = models.CharField(max_length=200)
    # reminder_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)