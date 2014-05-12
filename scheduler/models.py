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
		('Custm', 'Custom'),
		('Stocks', 'Stocks'),
		# ('Weather', 'Weather'),
	)

	MINUTES_CHOICES = (
		(0, '00'),
		(1, '01'),
		(2, '02'),
		(3, '03'),
		(4, '04'),
		(5, '05'),
		(6, '06'),
		(7, '07'),
		(8, '08'),
		(9, '09'),
		(10, "10"),
		(11, "11"),
		(12, "12"),
		(13, "13"),
		(14, "14"),
		(15, "15"),
		(16, "16"),
		(17, "17"),
		(18, "18"),
		(19, "19"),
		(20, "20"),
		(21, "21"),
		(22, "22"),
		(23, "23"),
		(24, "24"),
		(25, "25"),
		(26, "26"),
		(27, "27"),
		(28, "28"),
		(29, "29"),
		(30, "30"),
		(31, "31"),
		(32, "32"),
		(33, "33"),
		(34, "34"),
		(35, "35"),
		(36, "36"),
		(37, "37"),
		(38, "38"),
		(39, "39"),
		(40, "40"),
		(41, "41"),
		(42, "42"),
		(43, "43"),
		(44, "44"),
		(45, "45"),
		(46, "46"),
		(47, "47"),
		(48, "48"),
		(49, "49"),
		(50, "50"),
		(51, "51"),
		(52, "52"),
		(53, "53"),
		(54, "54"),
		(55, "55"),
		(56, "56"),
		(57, "57"),
		(58, "58"),
		(59, "59"),
	)

	user = models.ForeignKey(AuthUser)
	type = models.CharField(choices = MESSSAGE_CHOICES, default = 'Custom', max_length = 15)
	message = models.TextField(max_length = 150, blank = True, default = '')
	frequency = models.CharField(choices = FREQUENCY_CHOICES, default = 'ONE_OFF', max_length = 10)
	day_of_week = models.CharField(max_length = 10, blank=True, default = '')
	paused_at = models.DateTimeField(blank=True, null=True, default= None)
	start_date = models.DateField(default=datetime.date.today)
	hour = models.IntegerField(choices = HOUR_CHOICES, default= 12)
	minute = models.IntegerField(choices = MINUTES_CHOICES, default = 0)

	#minute = models.IntegerField(choices = [(i,i) for i in range(60)], default = 0)
	
	#blank = True means in the form you don't necessary need this field. 


	
# i=10
# for i in range (60):
# 	print '(' + str(i) + ', ' + '"' + str(i) + '"' + ')' + ','















