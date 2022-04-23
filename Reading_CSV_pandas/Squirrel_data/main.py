import pandas
import os
os.system("cls")

data = pandas.read_csv("squirrel_data.csv")

color_list = data["Primary Fur Color"].to_list()


color_dict = {}
for color in color_list:
    color_dict.setdefault(color, 0)
    color_dict[color] += 1

fur_color = []
count = []
for key, value in color_dict.items():
    fur_color.append(key)
    count.append(value)

del fur_color[0] #deletes the nan
del count[0] #deletes the count of nan

c_dict = {
    "Fur color" : fur_color,
    "Count" : count
}
new_data = pandas.DataFrame(c_dict)
new_data.to_csv("squirrel_colors.csv")
