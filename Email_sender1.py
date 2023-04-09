from email.message import EmailMessage
import ssl
import smtplib


email_sender = "razarajpoot99598@gmail.com"
password = "jzcjcaavacfgpjaa"

email_reciever = "razarajpoot9959@gmail.com"

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


