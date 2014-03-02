# Create your views here.
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
from scheduler.models import *
from scheduler.forms_scheduler import *

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
			new_schedule.save()
			return HttpResponseRedirect('/set_schedule')

	latest_schedule = Schedule.objects.all().filter(user=request.user)
	print latest_schedule

	return render (request, 'set_schedule.html', {'form': form, 'latest_schedule': latest_schedule},)

	