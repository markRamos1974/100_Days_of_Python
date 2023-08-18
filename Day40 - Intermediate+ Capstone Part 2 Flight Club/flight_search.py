from dotenv import load_dotenv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import requests

load_dotenv()

class FlightSearch:
    
    def __init__(self):
        self.KWIW_ENDPOINT = "https://api.tequila.kiwi.com/v2/"
        self.COUNTRY_CODE = "PH"
        self.DATE_NOW = datetime.now().strftime("%d/%m/%Y")
        self.DATE_RANGE = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")
        self.headers = {
            "Content-Type": "application/json",
            "apikey": os.environ.get("KIWI_API_KEY"),
            "Content-Encoding": "gzip"
        }

    def get_fight_deals_data(self, destination):
        search_enpoint = f"{self.KWIW_ENDPOINT}search"
        search_params = {
            "fly_from": self.COUNTRY_CODE,
            "fly_to": destination,
            "date_from": self.DATE_NOW,
            "date_to": self.DATE_RANGE,
            "limit": 10,
            "return_from": (datetime.now() + relativedelta(days=+7)).strftime("%d/%m/%Y"),
            "return_to": (datetime.now() + relativedelta(days=+28)).strftime("%d/%m/%Y")
        }
        

        response = requests.get(url=search_enpoint, params=search_params, headers=self.headers)
        response = response.json()["data"]
        return response
    
    def get_code_location(self, location):
        location_endpoint = f"https://api.tequila.kiwi.com/locations/query"
        
        parameters = {
            "term": location,
            "limit": 1,
            "local": "en-US",
            "location_types": "airport",
            "active_only": True
        }



        response = requests.get(url=location_endpoint, params=parameters, headers=self.headers)
        response = response.json()["locations"][0]["city"]["code"]

        return response
    
        