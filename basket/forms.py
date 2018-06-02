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
		fields = ['rut','dv','name','age','email','nickname','team','user']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PayrollForm(ModelForm):
	class Meta:
		model = Payroll
		fields = ['player','coach','name','date','time']