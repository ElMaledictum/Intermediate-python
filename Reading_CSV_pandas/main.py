import os
import csv
import pandas
os.system("clear")

# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file) #creates a csv reader object
#     t = []

#     for i in data:
#         if i[1] != "temp":
#             t.append(int(i[1]))
#     print (t)

# data = pandas.read_csv("weather_data.csv")
# print (data["temp"])

# data_dict = data.to_dict()
# print (data_dict)

# t_list = data["temp"].to_list()
# print (f"Average: {data['temp'].mean()}")

# print (data.condition)

# print (data[data.day == "Tuesday"]) #gets the row where the day equals "Tuesday"

# print (data[data.temp == data.temp.max()]) #returns the row where the temp is max


# monday = data[data.day == "Monday"]
# to_f = int(monday.temp) * (9/5) + 32
# print (to_f)

#create dataframe from scratch

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [77, 76, 79]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")

data = pandas.read_csv("birthdays.csv")

t = (6, 1)
d = {(item["month"], item["day"]):item for index,item in data.iterrows()}
person = d[t]
print (person["name"])
