#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
from reminderapp import views
from authentication import views_authentication as auth
from django.contrib.auth.views import login, logout
from scheduler import views_scheduler as scheduler


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reminderapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^user_data/$', views.user_data),
    url(r'^$', views.view_user_info), 
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^signup/', auth.signup), 
    url(r'^login/', auth.login_user), 
    url(r'^logout/', auth.logout), 
    
    url(r'^user_settings/$', views.view_user_info),
    url(r'^edit_data/$', views.edit_user_data),    
    url(r'^edit_stocks/$', views.edit_stocks),
    url(r'^delete_stocks/(\d{1,2})/$', views.delete_stock),
    url(r'^send_message/$', views.send_message),

    url(r'^set_schedule/$', scheduler.set_schedule),
    url(r'^delete_schedule/(\d{1,2})/$', scheduler.delete_schedule),


)



