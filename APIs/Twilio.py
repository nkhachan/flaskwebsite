from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC679fe8bb6316173299b8210a1f9101d4'
auth_token = ''
client = Client(account_sid, auth_token)

def sendSMS(message, phonenumber):

    message = client.messages.create(
                                  from_='+19404681770',
                                  body= message,
                                  to=phonenumber
                              )