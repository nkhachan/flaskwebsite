import sendgrid
import os
from sendgrid.helpers.mail import *


def sendEmail():
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email("noopur.khachane@gmail.com")
    to_email = Email("noopur.khachane@gmail.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

sendEmail()
