# Create your views here.
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #new_user = authenticate(username = request.POST['email'], password = request.POST['password'])
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form,})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

def login(request):
    
    errors =[]

    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = email, password = password)

    if request.method == 'POST':
	    if user is not None and user.is_active:
	        auth.login(request, user)
	        if 'next' in request.POST:
	            errors.append('in the if')
	            next = request.POST['next']
	            return HttpResponseRedirect(next)
	        else: 
	            return HttpResponseRedirect("/")
    else:
    	errors.append('') #write an email/password do not match error msg
    return render(request, 'login.html', {'errors': errors})


