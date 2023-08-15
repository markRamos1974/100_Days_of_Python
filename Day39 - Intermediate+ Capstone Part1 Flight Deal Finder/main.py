from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight_search = FlightSearch()
flight_sheet_data = FlightData()
notif = NotificationManager()
google_sheet_data = flight_sheet_data.read_sheet_data()


def update_flight_code():
    for flight_data in google_sheet_data:
        for (key, value) in flight_data.items():
            if key == "city":
                country_code = flight_search.get_code_location(value)
                row_id = flight_data["id"]
                flight_sheet_data.update_sheet_data(row_id, country_code)


for data in google_sheet_data:
    flight_deals = flight_search.get_fight_deals_data(data["iataCode"])[0]

    lowest_price_sheet = float(data["lowestPrice"])
    flight_price = float(flight_deals["price"])

    flight_from = flight_deals["cityFrom"]
    flight_country = flight_deals["cityTo"]
    flight_diff = lowest_price_sheet - flight_price


    if flight_price < lowest_price_sheet:
        notif.create_message(country_from=flight_from, country_to=flight_country, deal_diff=flight_diff)
        print(f"{flight_from} --> {flight_country} is less by {flight_diff} SMS SENT")
    else:
        print(f"{flight_from} --> {flight_country}: X")

   


    











