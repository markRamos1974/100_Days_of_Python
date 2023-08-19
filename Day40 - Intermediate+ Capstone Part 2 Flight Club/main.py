from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager
import smtplib

flight_search = FlightSearch()
flight_sheet_data = DataManager()

google_sheet_data_prices = flight_sheet_data.read_country_sheet_data()
google_sheet_data_users = flight_sheet_data.read_user_sheet_data()

notif = NotificationManager(google_sheet_data_users)

def update_flight_code():
    for flight_data in google_sheet_data_prices:
        for (key, value) in flight_data.items():
            if key == "city":
                country_code = flight_search.get_code_location(value)
                row_id = flight_data["id"]
                flight_sheet_data.update_sheet_data(row_id, country_code)

def send_message():
    flight_diff = round(lowest_price_sheet - flight_price)
    
    notif.create_message(

        country_from=flight_from, 
        country_to=flight_country, 
        deal_diff=flight_diff, 
        country_code_from=country_code_from, 
        country_code_to=country_code_to
    )
    print("Success message send")


# print("Welcome to Mark's Flight Club\nWe find the best flight deals and email you.")
# first_name = input("What is your first name?: ")
# last_name = input("What is your last name?: ")
# email = input("please enter your email address: ")
# phone_number = input("please enter your mobile number: ")

# flight_sheet_data.add_user(first_name=first_name, last_name=last_name, email=email, phone=phone_number)

for data in google_sheet_data_prices:
    flight_deal_data = flight_search.get_fight_deals_data(data["iataCode"])[0]
    flight_deals = FlightData(flight_deal_data)

    lowest_price_sheet = float(data["lowestPrice"])
    flight_price = flight_deals.price_GBP
    flight_from = flight_deals.city_from
    flight_country = flight_deals.city_to
    country_code_from = flight_deals.city_code_from
    country_code_to = flight_deals.city_code_to
    departure_date =  flight_deals.departure_date
    arrival_date =  flight_deals.arrival_date
    via_cities = ", ".join(flight_deals.via_cities)
    stop_overs = flight_deals.stop_over

    message_body = f"Low Price alert! Only £{flight_price} to fly from {flight_from}-{country_code_from} to {flight_country}-{country_code_to}, from {departure_date} to {arrival_date}."
    stop_over_message = f"Flight has {stop_overs} stop over, via {via_cities}\n"
    
    def display_flight_offers():
        print(f"Low Price alert! Only £{flight_price} to fly from {flight_from}-{country_code_from} to {flight_country}-{country_code_to}, from {departure_date} to {arrival_date}.")
    

    
    if flight_price < lowest_price_sheet:
       
        if stop_overs > 1:
            display_flight_offers()
            print(stop_over_message)
        else: 
            display_flight_offers()
            print("\n")

        print("sending Email...")
        notif.send_email(message_body, stop_over_message, stop_overs)
        print("sending SMS...")
        send_message()