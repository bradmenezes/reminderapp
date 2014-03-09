#Models for Scheduler App

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from reminderapp.models import TimeStampedModel
from django.contrib.auth.models import User as AuthUser

# Create your models here.
class Schedule(TimeStampedModel):
	
	FREQUENCY_CHOICES = (
		('DAILY', 'Daily'),
		('WEEKLY', 'Weekly'),
		('WEEKDAYS', 'Weekdays'),
		('WEEKENDS', 'Weekends'),
	)

	user = models.ForeignKey(AuthUser)
	message = models.CharField(max_length = 160)
	frequency = models.CharField(choices = FREQUENCY_CHOICES, default = 'WEEKLY', max_length = 10)
	day_of_week = models.CharField(max_length = 10)
	start_date = models.DateField()
	hour = models.IntegerField(
		validators=[
			MaxValueValidator(24),
			MinValueValidator(0),
		]
	)
	minute = models.IntegerField(
			validators=[
				MaxValueValidator(60),
				MinValueValidator(0),
			]
		)
	

















