# Models for ReminderApp App

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
#from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User as AuthUser
# import datetime
# from datetime import DateTimeField

class TimeStampedModel(models.Model):
	created_on = models.DateTimeField(auto_now_add = True)
	modified_date = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

class Stocks(TimeStampedModel):
	user = models.ForeignKey(AuthUser)
	stock = models.CharField(max_length=6)

class KeyUserData(TimeStampedModel):
	user = models.ForeignKey(AuthUser)
	zip_code = models.CharField(max_length = 6, default = '')
	phone_number = models.CharField(max_length = 10, default = '')
