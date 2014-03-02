from django import forms
from django.forms import ModelForm
from scheduler.models import *

class SchedulerForm(ModelForm):
	class Meta:
		model = Schedule
		exclude = ('day_of_week', 'user')


