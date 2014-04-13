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
		(24, '12 midnight'),
		
	)

	MESSSAGE_CHOICES = (
		('Custom', 'Custom'),
		('Stocks', 'Stocks'),
		('Weather', 'Weather'),
	)

	user = models.ForeignKey(AuthUser)
	message = models.TextField(max_length = 160)
	frequency = models.CharField(choices = FREQUENCY_CHOICES, default = 'WEEKLY', max_length = 10)
	day_of_week = models.CharField(max_length = 10, null=True, blank = True)
	start_date = models.DateField(default=datetime.date.today)
	hour = models.IntegerField(choices = HOUR_CHOICES, default= 6)
	minute = models.IntegerField(choices = [(i,i) for i in range(60)], default = 0)
	

















