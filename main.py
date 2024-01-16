# with open('weather_data.csv') as data:
#     weather = data.readlines()
#
# import csv
# data = csv.reader(weather)
# temperature = []
# for row in data:
#     temperature.append(row[1])

import pandas as pd

# data = pandas.read_csv("weather_data.csv")
# # data_list = data["temp"].to_list()
# # summation = 0
# # n = len(data_list)
# # for each in data_list:
# #     summation += each
# # average = summation/n
# # print(average)
#
# print(data.temp.max())
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_gray = len(data[data["Primary Fur Color"] == "Gray"])
data_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
data_black = len(data[data["Primary Fur Color"] == "Black"])
print(data_gray, data_black, data_red)

data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [data_gray, data_red, data_black]
}

df = pd.DataFrame(data_dict)
csv_data = df.to_csv("squirrel_count.csv")

