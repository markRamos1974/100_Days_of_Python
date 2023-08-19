from dotenv import load_dotenv
import os
from twilio.rest import Client
import smtplib
load_dotenv()

class NotificationManager:
    
    
    def __init__(self, users):
        self.TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
        self.AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.TWILIO_SID, self.AUTH_TOKEN)
        self.users = users

    def create_message(self, country_from, country_to, country_code_from, country_code_to, deal_diff):
        
        body_message = f"Book your flight now in {country_from}-{country_code_from} --> {country_to}-{country_code_to} for {deal_diff} less book now!"
        
        self.client.messages.create( 
            from_='+13344909407',
            body=body_message,
            to=f"+639619551081"
        )
        
        print("SMS Message sent")

    def send_email(self, message_body, stop_over_message, stop_overs):

        email = os.environ.get("EMAIL")
        password = os.environ.get("APP_PASSWORD")
        
        if stop_overs > 1:

            for user in self.users:
                first_name = user['firstName']
                message = f"Hello, {first_name},\n{message_body}, {stop_over_message}".encode("utf-8")

                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=email, password=password)
                    connection.sendmail(from_addr=email, to_addrs=user["email"], msg=message)
        else:

            for user in self.users:
                first_name = user["firstName"]
                message = f"Hello, {first_name},\n{message_body}".encode("utf-8")
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=email, password=password)
                    connection.sendmail(from_addr=email, to_addrs=user["email"], msg=message)
        
        print("Email Message sent")