from twilio.rest import Client

TWILIO_SID = "ACfe7c16fc27293c506866f6562ca47079"
TWILIO_AUTH_TOKEN = "136a9f34078fd6b2c577827d12d64d87"
TWILIO_VIRTUAL_NUMBER = "+17579097480"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"


#This class is responsible for sending notifications with the deal flight details.

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
