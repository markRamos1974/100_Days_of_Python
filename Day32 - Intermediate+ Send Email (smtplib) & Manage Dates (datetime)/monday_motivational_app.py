from datetime import datetime
import smtplib
import random

MY_EMAIL = "markadreianramos41@gmail.com"
RECIPIENT = "ramosmarkadreian39@gmail.com"
APP_PASSWORD = "aqtcylamuwwgjlvf"

def is_monday():
    today = datetime.now().weekday()

    if today == 1:
        return True
    return False



with open("quotes.txt", mode="r", encoding="utf-8") as quotes_file:
    data = quotes_file.readlines()

    
    if is_monday():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            random_quote = random.choice(data)
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=RECIPIENT, 
                msg=f"Subject:Monday Motivation Quote\n\n{random_quote}")



