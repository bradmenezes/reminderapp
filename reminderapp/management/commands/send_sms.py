from django.core.management.base import BaseCommand, CommandError
from apscheduler.scheduler import Scheduler
from reminderapp import views
import logging
from reminderapp.models import *
from scheduler.models import Schedule  

logging.basicConfig()
#phone_number = '+14155279628'

user_list = list(AuthUser.objects.all())
phone_number = '+14155279628'

class Command(BaseCommand):
    #def doit(self, sched, user_message):
    def handle(self, *args, **options):
        sched = Scheduler()
        sched.start()

        from twilio.rest import TwilioRestClient
        account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
        auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
        client = TwilioRestClient(account_sid, auth_token)

        for user in user_list:
            user_schedule = Schedule.objects.all().filter(user=user)
            for schedule in user_schedule:
                day_of_week = schedule.day_of_week
                hour = schedule.hour
                minute = schedule.minute
                user_message = schedule.message
                print 'BEFORE:' + str(user_message)
                
                def timed_job(msg):
                    print 'AFTER' + str(msg)
                sched.add_cron_job(lambda: timed_job(user_message), second='0-60')

        #sched.start()
        print 'test'
        while True:
            pass
