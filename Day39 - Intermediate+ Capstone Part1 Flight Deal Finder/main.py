from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager

flight_search = FlightSearch()
flight_sheet_data = DataManager()
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
    flight_deal_data = flight_search.get_fight_deals_data(data["iataCode"])[0]
    flight_deals = FlightData(flight_deal_data)

    lowest_price_sheet = float(data["lowestPrice"])
    flight_price = flight_deals.price_GBP
    flight_from = flight_deals.city_from
    flight_country = flight_deals.city_to
    

    if flight_price < lowest_price_sheet:
        flight_diff = round(lowest_price_sheet - flight_price)
        
        notif.create_message(

            country_from=flight_from, 
            country_to=flight_country, 
            deal_diff=flight_diff, 
            country_code_from=flight_deals.city_code_from, 
            country_code_to=flight_deals.city_code_to
        )
        
        print(f"{flight_from} --> {flight_country} is less by {flight_diff}GBP SMS SENT")
        print(f"{flight_deals.price_GBP}GBP < {lowest_price_sheet}GBP")
    else:
        print(f"{flight_from} --> {flight_country}: X")

   


    











