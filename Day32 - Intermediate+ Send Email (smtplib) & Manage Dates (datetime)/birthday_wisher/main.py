##################### Extra Hard Starting Project ######################
from datetime import datetime
import random
import smtplib
import pandas

# 1. Update the birthdays.csv
day = datetime.now().day
month = datetime.now().month

MY_EMAIL = "markadreianramos41@gmail.com"
APP_PASSWORD = "aqtcylamuwwgjlvf"

def generate_letter(name):
    random_letter_index = random.randint(1, 3)
    with open(f"./letter_templates/letter_{random_letter_index}.txt", mode="r") as data:
        letter_template = data.read()
        updated_letter = letter_template.replace("[NAME]", name)
        return updated_letter

# 2. Check if today matches a birthday in the birthdays.csv
person_index = 0
birthday_bank = pandas.read_csv("./birthdays.csv")
for name in birthday_bank["name"]:
    person = birthday_bank[birthday_bank["name"] == name].to_dict()

    person_month = person["month"][person_index]
    person_day = person["month"][person_index]
    person_email = person["email"][person_index]
    person_name = person["name"][person_index]

    if person_day == day and person_month == month:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            message = generate_letter(person_name)
            connection.starttls()
            connection.login(user=MY_EMAIL, password=APP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=person_email, msg=f"Subject:Happy Birthday!\n\n{message}")

    person_index += 1

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




