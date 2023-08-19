from dotenv import load_dotenv
import os
import requests

load_dotenv()

class DataManager():
        
    def __init__(self):
        self.SHEETY_ENDPOINT_PRICES = "https://api.sheety.co/05903529643691fd55dd3fe8b602bb78/flightDeals/prices"
        self.SHEETY_ENDPOINT_USERS = "https://api.sheety.co/05903529643691fd55dd3fe8b602bb78/flightDeals/users"
        self.AUTH_KEY = os.environ.get("SHEETY_FLIGHT_DEAL_AUTH")
        self.SHEETY_HEADERS = {
            "Authorization": f"Bearer {self.AUTH_KEY}"
        }

    def add_user(self, first_name, last_name, email, phone):
        new_user = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "phone": phone
            }
        }

        response = requests.post(url=self.SHEETY_ENDPOINT_USERS, headers=self.SHEETY_HEADERS, json=new_user)
        print(response.text)


    def read_user_sheet_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT_USERS, headers=self.SHEETY_HEADERS)
        response = response.json()["users"]
        
        return response


    def read_country_sheet_data(self):
        response = requests.get(url= self.SHEETY_ENDPOINT_PRICES, headers=self.SHEETY_HEADERS)

        response = response.json()["prices"]
        
        return response

    def update_country_code(self, id, code):
        sheety_update_endpoint = f"{ self.SHEETY_ENDPOINT_PRICES}/{id}"
        BODY = {
            "price": {
                "iataCode": code
            }
        }

        response = requests.put(url=sheety_update_endpoint, json=BODY, headers=self.SHEETY_HEADERS)
        print(response.text)


