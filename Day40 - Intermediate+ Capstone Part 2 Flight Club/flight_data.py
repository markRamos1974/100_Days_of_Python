class FlightData:
    
    def __init__(self, flight_data):
        self.city_from = flight_data["cityFrom"]
        self.city_code_from = flight_data["cityCodeFrom"]
        self.city_to = flight_data["cityTo"]
        self.city_code_to= flight_data["cityCodeTo"]
        self.price_EUR = round(int(flight_data["price"]))
        self.price_GBP = round(self.get_price_in_GBP())
        self.stop_over = len(flight_data["route"]) - 1
        self.via_cities = []
        self.departure_date = str(flight_data["local_departure"])[0:10]
        self.arrival_date = str(flight_data["local_arrival"])[0:10]
        
        self.routes = flight_data["route"].pop()

        if self.stop_over > 1:
            for route in flight_data["route"]:
                self.via_cities.append(route["cityTo"])
                
        
     

    def get_price_in_GBP(self):
        return self.price_EUR * 0.86

