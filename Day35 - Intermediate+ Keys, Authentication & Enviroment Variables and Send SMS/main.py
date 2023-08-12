import requests
import json
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("OPEN_WEATHER_API_KEY")
lat = 12.879721
lon = 121.774017

def get_current_weather():
    parameters = {
       "lat": lat,
       "lon": lon,
       "appid": api_key
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
    response = response.json()

    return response


weather_status = ""
with open("data.json") as weather_data:
    response = json.load(weather_data)
    response = response["weather"][0]
 
    weather_status = response["description"]


account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f"You will be experiencing {weather_status}",
    from_='+15736725680',
    to='+639922670248'
)



validation_request = client.validation_requests \
    .create(
         friendly_name='Mark Phone NUmber',
         status_callback='https://somefunction.twil.io/caller-id-validation-callback',
         phone_number='+639619551081'
     )

print(validation_request.validatio_code)