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
from django.core.mail import send_mail

@login_required(login_url = '/login')
def set_schedule(request):

	form = SchedulerForm(request.POST or None)

	frequency_to_day = {
		'DAILY': 'mon-sun',
		'WEEKLY': 'weekly',
		'WEEKENDS': 'sat-sun',
		'WEEKDAYS': 'mon-fri',
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
			
			# if schedule_to_edit.id:
			# 	new_schedule.id = schedule_to_edit.id

			new_schedule.save()
			return HttpResponseRedirect('/set_schedule')

	latest_schedule = Schedule.objects.all().filter(user=request.user)
	print latest_schedule	

	return render (request, 'set_schedule.html', {'form': form, 'latest_schedule': latest_schedule},)

@login_required(login_url = '/login')
def delete_schedule(request, schedule_id):
	Schedule.objects.get(pk = schedule_id).delete()
	return HttpResponseRedirect('/')

@login_required(login_url = '/login')
def sms_schedule(request, schedule_id):
	phone_number = str(KeyUserData.objects.all().get(user = request.user).phone_number)
	message = str(Schedule.objects.get(pk = schedule_id).message)

	phone_sms(request, message, phone_number)
	return HttpResponseRedirect('/set_schedule')


def email_schedule(request, schedule_id):
	message = str(Schedule.objects.get(pk = schedule_id).message)
	recipient = 'bmenezes@yelp.com'
	subject = 'DING: ' + message

	send_mail(subject, message,'bradmenezes10@gmail.com', [recipient],fail_silently=False)
	return HttpResponseRedirect('/set_schedule')

# def edit_schedule(request, schedule_id):
# 	try:
# 		schedule_to_edit = Schedule.objects.all().get(pk= schedule_id)
# 		form = SchedulerForm(request.POST or None, instance = schedule_to_edit)
# 	except Schedule.DoesNotExist:
# 		form = SchedulerForm(request.POST or None)

# 	if request.method == 'POST':
# 		set_schedule(request)
# 		return HttpResponseRedirect('/set_schedule')

# 	return render (request, 'set_schedule.html', {'form': form})










	