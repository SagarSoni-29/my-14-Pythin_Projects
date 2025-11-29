import smtplib
import ssl
from email.message import EmailMessage
EMAIL= "noorallawadi56@gmail.com"
APP_PASSWORD = "kvry tsse aaap agsz"
RECEIVER = "sagar1983soni@gmail.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Meassage from Sagar Soni , Very Important ."

msg.set_content("Hello I have send this E-Mail trough python code ")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(EMAIL,APP_PASSWORD)
    server.send_message(msg)