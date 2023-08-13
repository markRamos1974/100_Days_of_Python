import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
PIXELA_GRAPH_ID = os.environ.get("PIXEL_GRAPH_ID")
USER_HEADERS = {"X-USER-TOKEN": PIXELA_TOKEN}
# Creating account in pixela API
def create_pixela_acc():
    PIXELA_ENDPOINT = "https://pixe.la/v1/users"
    USER_PARAMETERS = {

        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME, 
        "agreeTermsOfService": "yes",
        "notMinor": "yes",

    }

    response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMETERS)
    print(response.text)

def create_pixela_graph():
    PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"
    GRAPH_CONFIG= {
        "id": "markramos41",
        "name": "Coding Habit Tracker",
        "unit": "commit",
        "type": "int",
        "color": "sora"
    }

    response = requests.post(url=PIXELA_GRAPH_ENDPOINT, headers=USER_HEADERS, json=GRAPH_CONFIG)
    print(response)

def create_commit_pixela(quantity):
    PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"   
    date = datetime.now().strftime("%Y%m%d")

    USER_BODY = {
        "date": date,
        "quantity": str(quantity),
    }
    response = requests.post(url=PIXELA_GRAPH_ENDPOINT, headers=USER_HEADERS, json=USER_BODY)
    print(response.text)

def updating_pixel(amount):
    date = datetime.now().strftime("%Y%m%d").replace("13", "15")
    PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{date}" 
    USER_BODY = {
        "quantity": str(amount)
    }

    response = requests.put(url=PIXELA_GRAPH_ENDPOINT, headers=USER_HEADERS, json=USER_BODY)
    print(response.text)

def delete_pixel():
    date = datetime.now().strftime("%Y%m%d")
    PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}/{date}" 
    print(PIXELA_GRAPH_ENDPOINT)

    response = requests.delete(url=PIXELA_GRAPH_ENDPOINT, headers=USER_HEADERS)
    print(response.text)

delete_pixel()