from scheduler.models import *  
from django.core.management.base import BaseCommand, CommandError
from apscheduler.scheduler import Scheduler as Scheduler
from reminderapp import views
import logging
from reminderapp.models import *
import datetime as dt
from datetime import datetime
from twilio.rest import TwilioRestClient
account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
client = TwilioRestClient(account_sid, auth_token)
logging.basicConfig()

class Command(BaseCommand):
    
    def start_scheduled_job(self, sched, user_message, phone_number, day_of_week, hour, minute, month, year, day_of_month, frequency, start_date):
        
        def send_message():
            print 'AFTER' + str(user_message) + str(phone_number)
            client.sms.messages.create(
                body= str(user_message),
                to= str(phone_number),
                from_= '+16502674790')

        #Depending on Frequency, set cron job for APScheduler 
        print user_message

        start_date = datetime(year, month, day_of_month)
        date_today = datetime.today()

        start_datetime = datetime(year, month, day_of_month, hour, minute)
        datetime_today = dt.datetime.now()

        print 'Start_date = ' + str(start_date)
        print 'date_today = ' + str(date_today) + '\n'       
        print 'Start_datetime = ' + str(start_datetime)
        print 'datetime_today = ' + str(datetime_today)

        #do a conditional based on dates of start <- date of today

        if start_date <= date_today: 
            print 'Weekly or Daily or something'
            if frequency == 'WEEKLY' or  frequency == 'DAILY' or  frequency =='WEEKENDS' or frequency == 'WEEKDAYS':
                print 'starting cron for weekly, daily or something'
                sched.add_cron_job(send_message, day_of_week = day_of_week, hour = hour, minute = minute)
                print 'Cron done for weeekly, daily or something'
            elif frequency == 'MONTHLY':
                sched.add_cron_job(send_message, day = day_of_month, hour = hour, minute = minute)
            elif frequency == 'YEARLY':
                sched.add_cron_job(send_message, month = month, day = day_of_month, hour = hour, minute = minute)
            elif frequency == 'ONE_OFF':
                print 'in One-off'
                if start_datetime >= datetime_today:
                    print 'condition worked!'
                    sched.add_date_job(send_message, datetime(year, month, day_of_month, hour, minute))

    def handle(self, *args, **options):
        sched = Scheduler()
        #Grab all the users in the db
        user_list = list(AuthUser.objects.all())
        #Loop through all the users
        for user in user_list:
            print 'This is for the user =' + str(user.username)
            #Grab the user Schedule and Number from the db
            try:
                user_schedule = Schedule.objects.all().filter(user=user)
                phone_number = str(KeyUserData.objects.all().get(user=user).phone_number)
                #For a given user, grab the varibles for the cron scheduler from each of thier schedules 
                for schedule in user_schedule:
                    day_of_week = schedule.day_of_week
                    hour = schedule.hour
                    minute = schedule.minute
                    user_message = schedule.message
                    month = schedule.start_date.month
                    start_date = schedule.start_date
                    year = schedule.start_date.year
                    day_of_month = schedule.start_date.day
                    frequency = schedule.frequency
                    if user == 'bmenezes':
                        print 'bmenezes you fucker!'
                    self.start_scheduled_job(sched, user_message, phone_number, day_of_week, hour, minute, month, year, day_of_month, frequency, start_date) 
            #If we don't have their Phone number or Schedule then Skip!
            except KeyUserData.DoesNotExist or Schedule.DoesNotExist:
                pass

        sched.start()
        while True:
            pass