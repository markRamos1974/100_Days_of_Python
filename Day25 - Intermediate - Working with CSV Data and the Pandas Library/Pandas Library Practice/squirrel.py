import pandas

squirrel_census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(squirrel_census_data[squirrel_census_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrel_census_data[squirrel_census_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_census_data[squirrel_census_data["Primary Fur Color"] == "Black"])

new_data = {

        "Fur Color" : ["Gray", "Red", "Black"],  
        "Count": [gray_count, cinnamon_count, black_count]
        
    }

new_csv = pandas.DataFrame(new_data)
new_csv.to_csv("Squirrel_Census.csv")
print(new_csv)


 