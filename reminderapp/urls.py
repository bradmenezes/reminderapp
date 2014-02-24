#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
from reminderapp import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reminderapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.view_user_info), 
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^user_data/$', views.user_data),
    url(r'^user_settings/$', views.view_user_info),
    url(r'^edit_stocks/$', views.edit_stocks),
    url(r'^delete_stocks/(\d{1,2})/$', views.delete_stock),
    url(r'^edit_user_data/$', views.edit_user_data),
    url(r'^send_message/$', views.send_message),
)



