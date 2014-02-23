from django import forms
from django.forms import ModelForm
from reminderapp.models import *

class ReviewCreationForm(ModelForm):
	class Meta:
		model = Review
		exclude = ('user')

class BusinessCreationForm(ModelForm):
	class Meta:
		model = Business 

class KeyUserDataForm(ModelForm):
	class Meta:
		model = KeyUserData
		exclude = ('user')

class StocksForm(ModelForm):
	class Meta:
		model = Stocks
		exclude = ('user')