class FlightData:
    
    def __init__(self, flight_data):
        self.city_from = flight_data["cityFrom"]
        self.city_code_from = flight_data["cityCodeFrom"]
        self.city_to = flight_data["cityTo"]
        self.city_code_to= flight_data["cityCodeTo"]
        self.price_EUR = round(int(flight_data["price"]))
        self.price_GBP = round(self.get_price_in_GBP())

    def get_price_in_GBP(self):
        return self.price_EUR * 0.86

