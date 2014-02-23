from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User as AuthUser
#from datetime import DateTimeField

class TimeStampedModel(models.Model):
	created_on = models.DateTimeField(auto_now_add = True)
	modified_date = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

class Stocks(TimeStampedModel):
	user = models.ForeignKey(AuthUser)
	stock = models.CharField(max_length = 4)

class KeyUserData(TimeStampedModel):
	user = models.ForeignKey(AuthUser, null = True)
	zip_code = models.CharField(max_length = 6)
	phone_number = PhoneNumberField()
