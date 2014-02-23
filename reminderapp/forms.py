from django import forms
from django.forms import ModelForm
from reminderapp.models import *

class KeyUserDataForm(ModelForm):
	class Meta:
		model = KeyUserData
		exclude = ('user')

class StocksForm(ModelForm):
	class Meta:
		model = Stocks
		exclude = ('user')