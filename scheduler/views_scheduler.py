# Create your views here.
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
from scheduler.models import *
from scheduler.forms_scheduler import * 
from reminderapp.views import *
from reminderapp.models import *
from django.core.mail import send_mail
import datetime

@login_required(login_url = '/login')
def set_schedule(request):

	form = SchedulerForm(request.POST or None)

	frequency_to_day = {
		'ONE_OFF': '',
		'DAILY': 'mon-sun',
		'WEEKLY': 'weekly',
		'WEEKENDS': 'sat-sun',
		'WEEKDAYS': 'mon-fri',
		'MONTHLY': '',
		'YEARLY': '',
	}

	if request.method == 'POST':
		if form.is_valid():
			new_schedule = form.save(commit=False)
			new_schedule.user = request.user 
			for key in frequency_to_day:
				if key == new_schedule.frequency:
					if key == 'WEEKLY':
						new_schedule.day_of_week = new_schedule.start_date.ctime().lower().partition(' ')[0]
					else: 
						new_schedule.day_of_week = frequency_to_day[key]

			new_schedule.save()
			return HttpResponseRedirect('/set_schedule')

	#Grab all schedules from db for this user
	latest_schedule = Schedule.objects.all().filter(user=request.user)
	
	#Remove One-off schedules that have passed.
	today = datetime.date.today()
	new_schedule = []
	for schedule in latest_schedule:
		if schedule.frequency =='ONE_OFF' and schedule.start_date < today:
			print 'Skip this one'
		else:
			new_schedule.append(schedule)

	#Define the frequencies a user has schedules on to group in template
	used_frequency = []
	for schedule in new_schedule:
		if schedule.frequency not in used_frequency:
			used_frequency.append(str(schedule.frequency))
	
	return render (request, 'set_schedule.html', 
				{'form': form, 
				'latest_schedule': new_schedule, 
				'used_frequency': used_frequency,})

@login_required(login_url = '/login')
def delete_schedule(request, schedule_id):
	Schedule.objects.get(pk = schedule_id).delete()
	return HttpResponseRedirect('/')

@login_required(login_url = '/login')
def sms_schedule(request, schedule_id):
	phone_number = str(KeyUserData.objects.all().get(user = request.user).phone_number)
	message = str(Schedule.objects.get(pk = schedule_id).message)

	phone_sms(message, phone_number)
	return HttpResponseRedirect('/')


def email_schedule(request, schedule_id):
	message = str(Schedule.objects.get(pk = schedule_id).message)
	recipient = 'bmenezes@yelp.com'
	subject = 'DING: ' + message

	send_mail(subject, message,'bradmenezes10@gmail.com', [recipient],fail_silently=False)
	return HttpResponseRedirect('/set_schedule')

def edit_schedule(request, schedule_id):
	

	frequency_to_day = {
		'ONE_OFF': '',
		'DAILY': 'mon-sun',
		'WEEKLY': 'weekly',
		'WEEKENDS': 'sat-sun',
		'WEEKDAYS': 'mon-fri',
		'MONTHLY': '',
		'YEARLY': '',
	}

	try:
		schedule_to_edit = Schedule.objects.all().get(pk= schedule_id)
		form = SchedulerForm(request.POST or None, instance = schedule_to_edit)
	except Schedule.DoesNotExist:
		form = SchedulerForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			new_schedule = form.save(commit=False)
			new_schedule.user = request.user 
			for key in frequency_to_day:
				if key == new_schedule.frequency:
					if key == 'WEEKLY':
						new_schedule.day_of_week = new_schedule.start_date.ctime().lower().partition(' ')[0]
					else: 
						new_schedule.day_of_week = frequency_to_day[key]

			new_schedule.save()
			return HttpResponseRedirect('/set_schedule')

	return render (request, 'edit_schedule.html', {'form': form})



#fake comment

#Load mobile page
@login_required(login_url = '/login')
def mobile_instructions(request):
	return render(request, 'mobile_instructions.html',)

#SMS the user instruction of how to get it on their phone
def mobile_sms(request):
	phone_number = str(KeyUserData.objects.all().get(user = request.user).phone_number)

	instructions_message = '1. Click the link\n2. Click the box with arrow icon\n3. Add to Home Screen'
	phone_sms(instructions_message, phone_number)	

	link_message = 'http://shrouded-peak-4089.herokuapp.com'
	phone_sms(link_message, phone_number)

	return HttpResponseRedirect('/mobile')

def send_stocks_sms(user, phone_number):

	message = ''

	try:
		latest_user_stocks_list = Stocks.objects.all().filter(user = user)
		print latest_user_stocks_list
		print 'in the try'
		for stock in latest_user_stocks_list:
			stock_price = round(float(ystockquote.get_price(stock.stock)),2)
			stock_symbol = (stock.stock).upper()
			message += str(stock_symbol) + ' $' + str(stock_price) + '\n'
			print len(message)

			if len(message) >= 150:
				phone_sms(message, phone_number)
				message = ''
		if message != '':
			phone_sms(message, phone_number)
	except Stocks.DoesNotExist:
		print 'hey'


