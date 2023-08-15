from dotenv import load_dotenv
import os
import requests

load_dotenv()

class FlightData:
    
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/91c045909d1ea9fd78de474cfedd4df1/flightDeals/prices"
        self.AUTH_KEY = os.environ.get("SHEETY_FLIGHT_DEAL_AUTH")
        self.SHEETY_HEADERS = {
            "Authorization": f"Bearer {self.AUTH_KEY}"
        }

    def read_sheet_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.SHEETY_HEADERS)
        response = response.json()["prices"]
        
        return response

    def update_sheet_data(self, id, code):
        sheety_update_endpoint = f"{self.SHEETY_ENDPOINT}/{id}"
        BODY = {
            "price": {
                "iataCode": code
            }
        }

        response = requests.put(url=sheety_update_endpoint, json=BODY, headers=self.SHEETY_HEADERS)
        print(response.text)
