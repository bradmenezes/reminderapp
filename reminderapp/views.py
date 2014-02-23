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
	print 'Hey Brad'
	latest_user_data_list = KeyUserData.objects.all().filter(user = AuthUser)
	latest_user_stocks_list = Stocks.objects.all().filter(user = AuthUser)

	latest_user_stocks_list = list(latest_user_stocks_list)

	for stock in latest_user_stocks_list:
		stock.price = round(float(ystockquote.get_price(stock.stock)),2)
		stock.stock = (stock.stock).upper()

		print stock.price
			
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

def send_message(request):
	
	zip_code = KeyUserData.objects.all().get(user = request.user).zip_code
	weather_text = get_weather(request, zip_code)
	
	stocks_list = list(Stocks.objects.all().filter(user = request.user))
	stock_text = getting_stocks(request, stocks_list)

	message = weather_text + '\n' + stock_text
	phone_number = KeyUserData.objects.all().get(user = request.user).phone_number
	print phone_number
	phone_sms (request, message, phone_number)
	
	return HttpResponseRedirect('/reviews')
