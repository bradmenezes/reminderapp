from django.contrib import admin
from django.contrib.auth.models import User
from reminderapp.models import *
from scheduler.models import *

#from reviews.models import Review, Business, User_data

class StocksAdmin(admin.ModelAdmin):
    list_display = ('user', 'stock', 'created_on', 'modified_date')

class KeyUserDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'zip_code', 'phone_number', 'created_on', 'modified_date')

admin.site.register(KeyUserData, KeyUserDataAdmin)
admin.site.register(Stocks, StocksAdmin)

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('user','type', 'frequency', 'message', 'paused_at', 'start_date', 'hour', 'minute', 'created_on', 'modified_date', 'day_of_week', )

admin.site.register(Schedule, ScheduleAdmin)
