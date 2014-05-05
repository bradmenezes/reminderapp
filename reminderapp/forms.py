from django import forms
from django.forms import ModelForm
from reminderapp.models import *

class KeyUserDataForm(ModelForm):
	zip_code = forms.CharField(max_length=6, min_length=6)
	phone_number = forms.CharField(max_length=10, min_length=10)
	class Meta:
		model = KeyUserData
		exclude = ('user')

class StocksForm(ModelForm):
	
	class Meta:
		model = Stocks
		exclude = ('user')