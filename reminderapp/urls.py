#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
from reminderapp import views
from authentication import views_authentication as auth
from django.contrib.auth.views import login, logout
from scheduler import views_scheduler as scheduler


urlpatterns = patterns('',

    url(r'^$', views.view_user_info), 
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^signup/', auth.signup), 
    url(r'^login/', auth.login_user), 
    url(r'^logout/', auth.logout), 
    
    url(r'^user_settings/$', views.view_user_info),
    url(r'^edit_data/$', views.edit_user_data),    
    url(r'^edit_stocks/$', views.edit_stocks),
    url(r'^delete_stocks/(\d{1,6})/$', views.delete_stock),
    url(r'^send_message/$', views.send_message),

    url(r'^set_schedule/$', scheduler.set_schedule),
    url(r'^delete_schedule/(\d{1,6})/$', scheduler.delete_schedule),
    url(r'^sms_schedule/(\d{1,6})/$', scheduler.sms_schedule),
    url(r'^email_schedule/(\d{1,6})/$', scheduler.email_schedule),
    url(r'^edit_schedule/(\d{1,6})/$', scheduler.edit_schedule),
    url(r'^mobile/$', scheduler.mobile_instructions),
    url(r'^mobile_sms/$', scheduler.mobile_sms),
    url(r'^pause_schedule/(\d{1,6})/$', scheduler.pause_schedule),
    url(r'^resume_schedule/(\d{1,6})/$', scheduler.resume_schedule),
)



