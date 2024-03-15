
#otp session
from email.message import EmailMessage
import ssl,smtplib

#otp=random.randint[1111,9999]
def send_email(otp,email,subjecttype):
   email_sender='nithin4593@gmail.com'
   email_password='xhgs gczq iidr srhx'
   email_receiver=email
   subject="Yelagiri Travels : Signup OTP"

   if (subjecttype=='1'):
      subject="Yelagiri Travels : Signup OTP"
      body=('Your otp is :'+str(otp))
   elif (subjecttype=='2'):
      subject="Yelagiri Travels : Reset password"
      body=('Your otp is :'+str(otp))
   elif (subjecttype=='3'):#Admin mail when new booking done
      subject=""
   
   em=EmailMessage()
   em['From']=email_sender
   em['To']=email_receiver
   em['Subject']=subject
   em.set_content(body)
   context=ssl.create_default_context()
   with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_password,email_receiver,em.as_string())