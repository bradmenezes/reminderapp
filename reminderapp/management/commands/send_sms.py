from django.core.management.base import BaseCommand, CommandError
from apscheduler.scheduler import Scheduler
#from reminderapp import views
import logging
from reminderapp.models import *

logging.basicConfig()
phone_number = '+14155279628'

class Command(BaseCommand):
    def handle(self, *args, **options):
        sched = Scheduler()

        from twilio.rest import TwilioRestClient
        account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
        auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
        client = TwilioRestClient(account_sid, auth_token)

        @sched.cron_schedule(day_of_week='sat',hour=14, minute=27)
        def scheduled_job():
            message = client.sms.messages.create(
            body='sat at 2 27',
            to=phone_number,    # Brad's Phone number
            from_="+16502674790")

        @sched.cron_schedule(day_of_week='mon-fri', hour=10, minute=5)
        def scheduled_job():
            message = client.sms.messages.create(
            body='Leave for work, 10:05',
            to=phone_number,    # Brad's Phone number
            from_="+16502674790")

        @sched.cron_schedule(day_of_week='sat-sun', hour=14, minute=27)
        def scheduled_job():
            message = client.sms.messages.create(
            body='Go to the gym on the weekend, boss',
            to=phone_number,    # Brad's Phone number
            from_="+16502674790")

        sched.start()

        while True:
            pass


def phone_sms(text, number):
    
    from twilio.rest import TwilioRestClient
    account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
    auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
    client = TwilioRestClient(account_sid, auth_token)
    
    #if request.method == 'POST':
        #sms_text = request.POST.get('sms_text', '')
    sms_text = text
    message = client.sms.messages.create(
        body=sms_text,
        to=number,    # Brad's Phone number
        from_="+16502674790")

 # trigger = CronTrigger(year=year, month=month, day=day, week=week,
 #                              day_of_week=day_of_week, hour=hour,
 #                              minute=minute, second=second,
 #                              start_date=start_date)

# @sched.interval_schedule(minutes=3)
# def timed_job():
#     print 'This job is run every three minutes.'

# @sched.cron_schedule(day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print 'This job is run every weekday at 5pm.'


        # @sched.cron_schedule(day_of_week='fri', hour=9, minute=50)
        # def scheduled_job():
        #     phone_sms('Fri at 9 50', phone_number)

        # @sched.cron_schedule(day_of_week='mon-fri', hour=10, minute=5)
        # def scheduled_job():
        #     phone_sms('Leave for work. Weekdays at 10:05', phone_number)

        # @sched.cron_schedule(day_of_week='sat-sun', hour=10, minute=00)
        # def scheduled_job():
        #     phone_sms('Go to the gym on the weekend, boss', phone_number)

