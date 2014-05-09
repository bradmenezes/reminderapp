#Models for Scheduler App

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from reminderapp.models import TimeStampedModel
from django.contrib.auth.models import User as AuthUser
from django.contrib.admin.widgets import AdminDateWidget 
import datetime

# Create your models here.
class Schedule(TimeStampedModel):
	
	FREQUENCY_CHOICES = (
		('ONE_OFF', 'One-off'),
		('DAILY', 'Daily'),
		('WEEKLY', 'Weekly'),
		('WEEKDAYS', 'Weekdays'),
		('WEEKENDS', 'Weekends'),
		('MONTHLY', 'Monthly'),
		('YEARLY', 'Yearly'),
	)

	HOUR_CHOICES = (
		
		(0, '12 midnight'),
		(1, '1 am'),
		(2, '2 am'),
		(3, '3 am'),
		(4, '4 am'),
		(5, '5 am'),
		(6, '6 am'),
		(7, '7 am'),
		(8, '8 am'),
		(9, '9 am'),
		(10, '10 am'),
		(11, '11 am'),
		(12, '12 noon'),
		(13, '1 pm'),
		(14, '2 pm'),
		(15, '3 pm'),
		(16, '4 pm'),
		(17, '5 pm'),
		(18, '6 pm'),
		(19, '7 pm'),
		(20, '8 pm'),
		(21, '9 pm'),
		(22, '10 pm'),
		(23, '11 pm'),		
	)

	MESSSAGE_CHOICES = (
		('Custom', 'Custom'),
		('Stocks', 'Stocks'),
		# ('Weather', 'Weather'),
	)

	user = models.ForeignKey(AuthUser)
	type = models.CharField(choices = MESSSAGE_CHOICES, default = 'Custom', max_length = 15)
	message = models.TextField(max_length = 150, blank = True, default = '')
	frequency = models.CharField(choices = FREQUENCY_CHOICES, default = 'ONE_OFF', max_length = 10)
	day_of_week = models.CharField(max_length = 10, blank=True, default = '')
	paused_at = models.DateTimeField(blank=True, null=True, default= None)
	start_date = models.DateField(default=datetime.date.today)
	hour = models.IntegerField(choices = HOUR_CHOICES, default= 12)
	minute = models.IntegerField(choices = [(i,i) for i in range(60)], default = 0)
	


	#blank = True means in the form you don't necessary need this field. 















