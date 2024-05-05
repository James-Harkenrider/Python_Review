# data_list = []
# with open('weather_data.csv', 'r') as data:
#     for line in data.readlines():
#         data_list.append(line.strip())

# print(data_list)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except ValueError:
#             pass
# print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = data[data["Primary Fur Color"] == "Gray"]
red = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]
squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "count": [len(grey), len(red), len(black)]
}

squirrel_df = pandas.DataFrame(squirrel_dict)
squirrel_df.to_csv("squirrel_count.csv")
print(squirrel_df)

# data = pandas.read_csv("weather_data.csv")
# max_temp = data["temp"].max()
#
# row_max_temp = data[data.temp == max_temp]
#
# monday = data[data.day == "Monday"]
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_scratch = pandas.DataFrame(data_dict)
# print(data_scratch)


