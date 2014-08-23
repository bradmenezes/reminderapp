#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()
from reminderapp import views
from authentication import views_authentication as auth
from django.contrib.auth.views import login, logout
from scheduler import views_scheduler as scheduler

from tastypie.api import Api
from reminderapp.api import *


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ScheduleResource())

schedule_resource = ScheduleResource()

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

    #url(r'^blog/', include('reminderapp.urls')),
    #url(r'^api/', include(schedule_resource.urls)),
    url(r'^api/', include(v1_api.urls)),

    #url(r'^__debug__/', include(debug_toolbar.urls)),


)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#     url(r'^__debug__/', include(debug_toolbar.urls)),
# )



