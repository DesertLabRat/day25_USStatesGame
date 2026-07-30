import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(df.head())
# print(df["Primary Fur Color"].unique())
colors = df["Primary Fur Color"].unique()
new_dict = {}

for color in colors:
    # print(color)
    # print(type(color))
    try:
        count = df["Primary Fur Color"].value_counts()[color]
        new_dict[color] = count
    except KeyError:
        continue

# print(new_dict)
new_df = pd.DataFrame.from_dict(new_dict, orient="index").to_csv("squirrel_count.csv")
print(new_df)

# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         #use this method for skipping a known header row; con - not robust, only skips "temp"
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#         # more robust data cleaning, more pythonic; not good for skipping known header row
#         # try:
#         #     temperatures.append(int(row[1]))
#         # except ValueError:
#         #     continue
#
#     print(temperatures)

# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# print(data["temp"])

#convert df to dictionary
# data_dict = data.to_dict()
# print(data_dict)

#convert column to list
# temp_list = data["temp"].to_list()
# print(temp_list)

#long way of calculating mean of column
# mean = sum(temp_list) / len(temp_list)
# print(mean)

#pd way of calculating mean
# print(data["temp"].mean())
# print(data["temp"].max())

# row = data[data.day == "Monday"]
# print(data[data.temp == data.temp.max()])
# #or
# print(data.loc[data.temp.idxmax()])

# monday = data[data.day == "Monday"]
# print((9/5)*monday.temp + 32)

# data_dict = {
#     "students": [ "Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# df = pd.DataFrame(data_dict).to_csv("new_data.csv")
# print(df.head())