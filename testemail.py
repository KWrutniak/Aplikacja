import smtplib, ssl


port = 465
smtp_server = "smtp.gmail.com"
sender_mail = "aplikacjatestowa2@gmail.com"
recipient_email = "aplikacjatestowa2@gmail.com"
password = "fgdfjshigfcfqtyj"


contents = """/
From: <aplikacjatestowa2@gmail.com>
To: <aplikacjatestowa2@gmail.com>
Subject: testowy email

to jest wiadomość próbna
"""
contents  = contents.encode('utf-8')

ssl.connection = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context = ssl.connection) as server:
    server.login(sender_mail, password)
    server.sendmail (sender_mail, recipient_email, contents)