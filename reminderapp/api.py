#reminderapp/api.py 
from tastypie import fields
from scheduler.models import *
from django.contrib.auth.models import User
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from django.db import models

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		#fields = ['username', 'first_name', 'last_name', 'last_login'];
		allowed_method = ['get', 'post']
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']

		filtering = {
            'username': ALL,
        }

class ScheduleResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user')

	class Meta:
		queryset = Schedule.objects.all()
		resource_name = 'schedule'
		authorization = Authorization()
		filtering = {
            'user': ALL_WITH_RELATIONS,
        }

        def determine_format(self, request):
			return 'application/json'	


		# this is a test :)