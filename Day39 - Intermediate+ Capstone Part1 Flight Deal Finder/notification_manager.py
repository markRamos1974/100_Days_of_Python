from dotenv import load_dotenv
import os
from twilio.rest import Client
load_dotenv()

class NotificationManager:
    
    
    def __init__(self):
        self.TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
        self.AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.TWILIO_SID, self.AUTH_TOKEN)

    def create_message(self, country_from, country_to, deal_diff):
        body_message = f"Book your flight now in {country_from} --> {country_to} for {deal_diff} less book now!"
        message = self.client.messages.create( 
            from_='+13344909407',
            body=body_message,
            to='+639619551081'

        
        )

        print(message.status)