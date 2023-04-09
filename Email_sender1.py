"""
        EMAIL SENDER
        
        New way of sending mail by python.
        
        You need go to your gmail account and generate new app password.
        If you don't have libraries then simply install by this
        command: pip install smptlib ssl
        
        You don't need to install email.message because it is pre-install
        just import them.
"""


from email.message import EmailMessage
import ssl
import smtplib


email_sender = "Enter sender email address"
password = "Enter sender email app password"

email_reciever = "Enter receiver email address"

#email subject and body, you can change it according to your need.

subject = "Good Morning!"
body = """
    I hope this day is great for you. Do hard work, Stay positive and Stay blessed
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', context=context) as conn:
    conn.login(email_sender, password)
    conn.sendmail(email_sender, email_reciever, em.as_string())
    print("Email has been send successfully.")