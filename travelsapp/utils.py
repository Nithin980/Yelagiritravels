import pyotp
from datetime import datetime,timedelta
from email import *


from travelsapp.email import send_email

def send_otp(request):
    email=request.GET['email']
    subjecttype=request.GET['subjecttype']
    totp=pyotp.TOTP(pyotp.random_base32(),interval=120)
    otp=totp.now()
    print(f'Your otp: {otp}')
    request.session['otp_secret_key']=totp.secret
    valid_date=datetime.now()+timedelta(minutes=2)
    request.session['otp_valid_date']=str(valid_date)
    send_email(otp,email,subjecttype)
    return