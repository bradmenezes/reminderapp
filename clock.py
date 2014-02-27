from apscheduler.scheduler import Scheduler
from reminderapp import views

sched = Scheduler()

@sched.interval_schedule(minutes=1)
def timed_job():
    a = 'testing 1,2,3...'
    print a
    phone_sms (a, '+14155279628')

sched.start()

while True:
    pass
