travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, number_of_visit, cities_visited):
    new_item = {
        "country": country,
        "visits": number_of_visit,
        "cities": cities_visited,
    }

    travel_log.append(new_item)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
