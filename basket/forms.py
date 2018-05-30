from django.forms import ModelForm
from basket.models import *


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']

class TeamForm(ModelForm):
	class Meta:
		model = Team
		fields = ['name','description','logo','code']

class CoachForm(ModelForm):
	class Meta:
		model = Coach
		fields = ['rut','dv','name','age','email','nickname','team']		