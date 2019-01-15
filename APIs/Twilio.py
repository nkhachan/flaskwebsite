from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console

client = Client(account_sid, auth_token)

def sendSMS(message, phonenumber):

    message = client.messages.create(
                                  from_='+19404681770',
                                  body= message,
                                  to=phonenumber
                              )