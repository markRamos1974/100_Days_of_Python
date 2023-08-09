import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 12.879721 # Your latitude
MY_LONG = 121.774017 # Your longitude
MY_EMAIL = "markadreianramos41@gmail.com"
APP_PASSWORD = "aqtcylamuwwgjlvf"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_visible():
    return iss_latitude in range(int(MY_LAT) - 5, int(MY_LAT) + 5) and iss_longitude in range(int(MY_LONG) - 5, int(MY_LONG) + 5)



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


#If the ISS is close to my current position
while True:
    
    if is_iss_visible:
        print("Sending email...")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="ramosmarkadreian39@gmail.com", msg="Subject:Look up in the Sky.\n\nISS is visible from your current location")
            print("Email sent successfully...")
    time.sleep(2)

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



