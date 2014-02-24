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


def user_data(request):
	form = KeyUserDataForm(request.POST or None)
	
	if request.method == 'POST':
		if form.is_valid():
			new_user_data = form.save(commit = False)
			new_user_data.user = request.user
			new_user_data.save()
			print form
			return HttpResponseRedirect ('/reviews')
	
	return render (request, 'user_data.html', {'form': form})

def user(request):
	return {'user': request.user}

def view_user_info(request):
	AuthUser = request.user
	latest_user_data_list = KeyUserData.objects.all().filter(user = AuthUser)
	latest_user_stocks_list = Stocks.objects.all().filter(user = AuthUser)

	latest_user_stocks_list = list(latest_user_stocks_list)

	for stock in latest_user_stocks_list:
		stock.price = round(float(ystockquote.get_price(stock.stock)),2)
		stock.stock = (stock.stock).upper()
			
	return render(request,
		'view_settings.html',
		{'latest_user_data_list': latest_user_data_list, 
		'latest_user_stocks_list': latest_user_stocks_list},
	  	)

def delete_stock(request, stock_id):
	Stocks.objects.get(pk = stock_id).delete()
	return HttpResponseRedirect('/edit_stocks')

def edit_user_data(request):
	
	#Using try/except here since row may not exist yet
	try:
		user_data_to_edit = KeyUserData.objects.get(user = request.user)
		print 'exists!'
	except KeyUserData.DoesNotExist:
		print 'DoesNotExist'
		user_data_to_edit = None
		form = KeyUserDataForm(request.POST or None)
		form.user = request.user 
 	
	form = KeyUserDataForm(request.POST or None, instance = user_data_to_edit)


	if request.method == 'POST':
		if form.is_valid():
			changed_book = form.save()
			changed_book.save()
	        return HttpResponseRedirect('/user_settings')
	return render(request, 'user_data.html', {'form': form})

def getting_stocks(request, stocks_list):
	stock_prices = {}
	message = '\n'

	for stock in stocks_list:
		stock_prices[stock.stock] = round(float(ystockquote.get_price(stock.stock)),2)
		message += str(stock.stock) + ': ' + str(stock_prices[stock.stock]) + '\n'
	print message
	return message

def get_weather(request, zip_code):
    #import pywapi
    today = datetime.date.today()
    
    #Get weather from Yahoo Weather API
    weather = pywapi.get_weather_from_yahoo(zip_code)

    #Grab the temperature, high, low, description from the response
    temperature = weather['condition']['temp']
    high = weather['forecasts'][0]['high']
    low = weather['forecasts'][0]['low']
    description = weather['forecasts'][0]['text']
    
    #Save the SMS text as a string
    text = str(today) + '\n \n' + str(temperature) + ' and ' + str(description) + '\nfrom ' + str(high) + ' to ' + str(low) + '\n'
    return(text)

def send_message(request):
	
	zip_code = KeyUserData.objects.all().get(user = request.user).zip_code
	weather_text = get_weather(request, zip_code)
	
	stocks_list = list(Stocks.objects.all().filter(user = request.user))
	stock_text = getting_stocks(request, stocks_list)

	message = str(weather_text) + '\n' + str(stock_text)
	print type(message)

	phone_number = str(KeyUserData.objects.all().get(user = request.user).phone_number)
	print type(phone_number)
	phone_sms (request, message, phone_number)
	
	return HttpResponseRedirect('/user_data')

def phone_sms(request, text, number):

    from twilio.rest import TwilioRestClient
    
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
    auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
    client = TwilioRestClient(account_sid, auth_token)
    
    #if request.method == 'POST':
        #sms_text = request.POST.get('sms_text', '')
    sms_text = text
    
    message = client.sms.messages.create(
        body=sms_text,
        to=number,    # Brad's Phone number
        from_="+16502674790")

