from dotenv import load_dotenv
from datetime import datetime
import os
import requests

load_dotenv()

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com"
SHEETY_PROJECT_TOKEN = os.environ.get("SHEETY_PROJECT_TOKEN")
SHEETY_API_ENDPOINT = "https://api.sheety.co/91c045909d1ea9fd78de474cfedd4df1/myWorkouts/workouts"

user_input = input("Tell me what exercise you did: ")

def get_calories_burned_amount():
    global user_input
    ENDPOINT_EXTENSION = "/v2/natural/exercise"
    ENDPOINT = f"{NUTRITIONIX_ENDPOINT}{ENDPOINT_EXTENSION}"
    HEADERS = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "x-remote-user-id": "0",

    }
    BODY_CONFIG = {
        "query": user_input,
        "gender": "male",
        "weight_kg": 55,
        "height_cm": 156,
        "age": 21
    }
    response = requests.post(url=ENDPOINT, json=BODY_CONFIG,  headers=HEADERS)
    response = response.json()["exercises"]
    return response

exercises_data = get_calories_burned_amount()

def read_workoutsheet():
    HEADER = {
        "Authorization": f"Bearer {SHEETY_PROJECT_TOKEN}"
    }
    response = requests.get(url=SHEETY_API_ENDPOINT, headers=HEADER)
    response = response.json()
    print(response)

# read_workoutsheet()

def add_workout(excercise, calories_burned, duration):
    HEADER = {
        "Authorization": f"Bearer {SHEETY_PROJECT_TOKEN}"
    }
    print(datetime.now().strftime("%X"))
    BODY_CONFIG = {
        "workout": {
            "date": datetime.now().strftime("%m/%d/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": excercise,
            "calories": calories_burned,
            "duration": duration
        }   
    }

    response = requests.post(url=SHEETY_API_ENDPOINT, json=BODY_CONFIG, headers=HEADER)
    print(response.text)
    

# for workout in exercises_data:
#     print(workout)
#     workout_data = workout.items()
    
#     exercise = workout["name"]
#     duration = workout["duration_min"]
#     calories = workout["nf_calories"]

#     add_workout(excercise=exercise, duration=duration, calories_burned=calories)
