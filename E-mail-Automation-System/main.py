import os
import smtplib as s
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

ob=s.SMTP("smtp.gmail.com", 587)
ob.starttls()
ob.login(EMAIL_USER, EMAIL_PASS)

subject = "E-mail Automation Task!"

body = """Salam,

I am Marium Afzal, an intern at Apexcify Technologies (Remote).
This is my first Python internship task: Email Automation System.

Looking forward to growing and learning more during this internship.

Regards,  
Marium Afzal
"""

message="subject:{}\n\n{}".format(subject,body)
listofaddress=["mariumafzal.contact@gmail.com","apexcifytechnologys@gmail.com"]

ob.sendmail("EMAIL_USER", listofaddress,message)

print("send sucessfully")









