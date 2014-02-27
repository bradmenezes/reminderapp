from apscheduler.scheduler import Scheduler
#from /reminderapp import views

sched = Scheduler()

@sched.inteexitrval_schedule(minutes=1)
def timed_job():
    a = 'testing 1,2,3...'
    print a
    from twilio.rest import TwilioRestClient
    
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC6fe90756ae4096c5bf790984038a3f32"
    auth_token  = "97e8833ee3553bc4d9d16e86f1865d32"
    client = TwilioRestClient(account_sid, auth_token)
    
    #if request.method == 'POST':
        #sms_text = request.POST.get('sms_text', '')
    sms_text = a
    
    message = client.sms.messages.create(
        body=sms_text,
        to=+"14155279628",    # Brad's Phone number
        from_="+16502674790")

sched.start()

while True:
    pass
