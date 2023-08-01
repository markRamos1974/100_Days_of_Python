# with open("weather_data.csv") as data:
#     weather_conditions = data.readlines()
#     print(weather_conditions)

# import csv

# with open("weather_data.csv") as data:
#     weather_conditions = csv.reader(data)

#     temperatures = []
#     for weather_condition in weather_conditions:
#         for weather_temp in weather_condition[1:2]:
#             if weather_temp != "temp":
#                 temperatures.append(int(weather_temp))

#     print(temperatures)

import pandas

weather_data = pandas.read_csv("weather_data.csv")
data = weather_data[weather_data.day == "Monday"]
day_temp = int(data.temp)
farenheit = (day_temp * (9/5)) + 32

print(f"The temp today is {farenheit}")

