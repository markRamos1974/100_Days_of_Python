import requests
from datetime import datetime


ENDPOINT = "https://api.sunrise-sunset.org/json"
def send_request(endpoint):
    MY_LAT = 12.879721
    MY_LONG = 121.774017
    FORMATTED = 0
    request_url = f"{endpoint}?lat={MY_LAT}&ln={MY_LONG}&formatted={FORMATTED}"

    response = requests.get(request_url)
    response.raise_for_status()
    response = response.json()

    return response


sunset = send_request(ENDPOINT)["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = send_request(ENDPOINT)["results"]["sunrise"].split("T")[1].split(":")[0]

print(type(datetime.now().hour))
