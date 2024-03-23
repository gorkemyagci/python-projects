# Beginner Python Projects
# Email Sender

from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'wsdff345@otemdi.com'
email_password = '**** **** **** ****'
email_receiver = 'wepipat332@otemdi.com'

subject = 'Python Email Sender'
body = 'This is a test email sent from Python'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context==context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print('Email sent successfully')
    
