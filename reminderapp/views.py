from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from forms import *
from reminderapp.models import *
from django.template import RequestContext
import ystockquote
import datetime
from scheduler.models import *
from scheduler.forms_scheduler import * 

@login_required (login_url = '/login')
def edit_stocks(request):
	form = StocksForm(request.POST or None)
	AuthUser = request.user

	if request.method == 'POST':
		if form.is_valid():
			new_stock = form.save(commit= False)
			new_stock.user = AuthUser
			new_stock.save()
			return HttpResponseRedirect ('/edit_stocks')
	
	latest_user_stocks_list = Stocks.objects.all().filter(user = AuthUser)
	
	for stock in latest_user_stocks_list:
		stock.price = round(float(ystockquote.get_price(stock.stock)),2)
		stock.stock = (stock.stock).upper()

	return render (request, 'add_stocks.html', {'form': form, 'latest_user_stocks_list': latest_user_stocks_list},)
		#return render (request, 'write_a_review.html', {'form': form}, context_instance=RequestContext(request))


@login_required (login_url = '/login')
def edit_user_data(request):
	
	try:
		user_data_to_edit = KeyUserData.objects.get(user = request.user)
		print user_data_to_edit.phone_number
		user_data_to_edit.phone_number = user_data_to_edit.phone_number.replace("+1", "") 
		print user_data_to_edit.phone_number
		form = KeyUserDataForm(request.POST or None, instance = user_data_to_edit)
	except KeyUserData.DoesNotExist:
		form = KeyUserDataForm(request.POST or None)

	if request.method == 'POST':
		print 'hey'
		if form.is_valid():
			new_user_data = form.save(commit = False)
			new_user_data.user = request.user
			
			print new_user_data.phone_number
			new_user_data.phone_number = '+1' + str(new_user_data.phone_number)
			print new_user_data.phone_number
			new_user_data.save()
			return HttpResponseRedirect ('/')
	
	return render (request, 'user_data.html', {'form': form})

def user(request):
	return {'user': request.user}

@login_required (login_url = '/login')
def view_user_info(request):
	AuthUser = request.user.pk
	latest_user_data_list = KeyUserData.objects.all().filter(user = AuthUser)
	latest_user_stocks_list = Stocks.objects.all().filter(user = AuthUser)

	latest_user_stocks_list = list(latest_user_stocks_list)

	for stock in latest_user_stocks_list:
		stock.price = round(float(ystockquote.get_price(stock.stock)),2)
		stock.stock = (stock.stock).upper()
	
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

	frequency_to_day = {
		'ONE_OFF': '',
		'DAILY': 'mon-sun',
		'WEEKLY': 'weekly',
		'WEEKENDS': 'sat-sun',
		'WEEKDAYS': 'mon-fri',
		'MONTHLY': '',
		'YEARLY': '',
	}

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
			return HttpResponseRedirect('/')

	return render(request,
		'view_settings.html',
		{'latest_user_data_list': latest_user_data_list, 
		'latest_user_stocks_list': latest_user_stocks_list,
		'latest_schedule': new_schedule,
		'used_frequency': used_frequency,
		'form': form,
	  	})

@login_required (login_url = '/login')
def delete_stock(request, stock_id):
	Stocks.objects.get(pk = stock_id).delete()
	return HttpResponseRedirect('/edit_stocks')

def getting_stocks(request, stocks_list):
	stock_prices = {}
	message = '\n'

	for stock in stocks_list:
		stock_prices[stock.stock] = round(float(ystockquote.get_price(stock.stock)),2)
		message += str(stock.stock) + ': ' + str(stock_prices[stock.stock]) + '\n'
	print message
	return message

# def get_weather(request):
#     import pywapi
#     today = datetime.date.today()
#     user_zip_code = str(KeyUserData.objects.all().get(user = request.user).zip_code)
#     #Get weather from Yahoo Weather API

#     weather = pywapi.get_weather_from_yahoo(user_zip_code)

#     #Grab the temperature, high, low, dsescription from the response
#     temperature = weather['condition']['temp']
#     high = weather['forecasts'][0]['high']
#     low = weather['forecasts'][0]['low']
#     description = weather['forecasts'][0]['text']
    
#     #Save the SMS text as a string
#     text = str(today) + '\n \n' + str(temperature) + ' and ' + str(description) + '\nfrom ' + str(high) + ' to ' + str(low) + '\n'
#     phone_number = '+14155279628'
#     phone_sms(text, phone_number)
#     return HttpResponseRedirect('/')

@login_required (login_url = '/login')
def send_message(request):
	
	zip_code = KeyUserData.objects.all().get(user = request.user).zip_code
	#weather_text = get_weather(request, zip_code)
	
	stocks_list = list(Stocks.objects.all().filter(user = request.user))
	stock_text = getting_stocks(request, stocks_list)

	# add str(weather_text) when you figure out pywapi 
	message = '\n' + str(stock_text)
	print type(message)

	phone_number = str(KeyUserData.objects.all().get(user = request.user).phone_number)
	print type(phone_number)
	phone_sms (message, phone_number)
	
	return HttpResponseRedirect('/')

#def phone_sms(request, text, number):
def phone_sms(message, phone_number):

    from twilio.rest import TwilioRestClient
    
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
    auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
    client = TwilioRestClient(account_sid, auth_token)
    
    client.sms.messages.create(
        body=message,
        to=phone_number,
        from_="+16502674790")


