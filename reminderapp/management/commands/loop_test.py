#from scheduler.models import *  
from django.core.management.base import BaseCommand, CommandError
from apscheduler.scheduler import Scheduler as Scheduler
#from reminderapp import views
import logging
from reminderapp.models import *
from twilio.rest import TwilioRestClient
account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
client = TwilioRestClient(account_sid, auth_token)
logging.basicConfig()

sched = Scheduler()

def test():
    print 'Hey!'

sched.add_cron_job(test, day = 26, month = '1-12', day_of_week = 'mon-fri', second = '0-59')
print 'It worked!'

sched.start()

while True:
    pass


# class Command(BaseCommand):
    
#     def start_scheduled_job(self, sched, user_message, phone_number, day_of_week, hour, minute):
        
#         def send_message():
#             print 'AFTER' + str(user_message) + str(phone_number)
#             client.sms.messages.create(
#                 body= str(user_message),
#                 to= str(phone_number),
#                 from_= '+16502674790')

#         sched.add_cron_job(send_message, day_of_week = day_of_week, hour = hour, minute = minute)

#     def handle(self, *args, **options):
#         sched = Scheduler()
#         user_list = list(AuthUser.objects.all())
#         for user in user_list:
#             print 'This is for the user =' + str(user.username)
#             try:
#                 user_schedule = Schedule.objects.all().filter(user=user)
#                 phone_number = str(KeyUserData.objects.all().get(user=user).phone_number)
#                 for schedule in user_schedule:
#                     day_of_week = schedule.day_of_week
#                     hour = schedule.hour
#                     minute = schedule.minute
#                     user_message = schedule.message
#                     print str(day_of_week) + str(user_message)
#                     self.start_scheduled_job(sched, user_message, phone_number, day_of_week, hour, minute)
#             except KeyUserData.DoesNotExist or Schedule.DoesNotExist:
#                 pass
#                 #print 'For user= ' + str(user.username) + ' this failed'

#         sched.start()
#         while True:
#             pass