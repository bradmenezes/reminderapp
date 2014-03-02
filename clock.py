from apscheduler.scheduler import Scheduler
#from reminderapp import views
from reminderapp.models import *
import logging
logging.basicConfig()

sched = Scheduler()

user = list(AuthUser.objects.all())
print user

from twilio.rest import TwilioRestClient
account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
client = TwilioRestClient(account_sid, auth_token)

phone_number = '+14155279628'

@sched.interval_schedule(minutes=1)
def timed_job():
	print user
	print 'every minute'

@sched.cron_schedule(day_of_week='sat', hour=14, minute=32)
def scheduled_job():
    print 'sat at 2 30 - day of week sat'
    message = client.sms.messages.create(
    body='sat at 2 30',
    to=phone_number,    # Brad's Phone number
    from_="+16502674790")

@sched.cron_schedule(day_of_week='mon-fri', hour=14, minute=32)
def scheduled_job():
    print 'sat at 2 30 - day of week mon-fri'
    message = client.sms.messages.create(
    body='Leave for work, 10:05',
    to=phone_number,    # Brad's Phone number
    from_="+16502674790")

@sched.cron_schedule(day_of_week='sat-sun', hour=14, minute=32)
def scheduled_job():
    message = client.sms.messages.create(
    body='Go to the gym on the weekend, boss',
    to=phone_number,    # Brad's Phone number
    from_="+16502674790")

sched.start()

while True:
    pass

# def phone_sms(text, number):
	
#     from twilio.rest import TwilioRestClient
    
#     # Your Account Sid and Auth Token from twilio.com/user/account
#     account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
#     auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
#     client = TwilioRestClient(account_sid, auth_token)
    
#     #if request.method == 'POST':
#         #sms_text = request.POST.get('sms_text', '')
#     sms_text = text
    
#     message = client.sms.messages.create(
#         body=sms_text,
#         to=number,    # Brad's Phone number
#         from_="+16502674790")

