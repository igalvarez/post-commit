import smtplib

sender = 'from@example.com'
receivers = ['israel@localhost']
message = """From: From Person <from@example.com>
To: To Person <to@example.com>
Subject: SMTP email example


This is a test message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
except SMTPException:
    pass
