from prettytable import PrettyTable
from os import system
system('cls')


x = PrettyTable()

x.field_names = ["Pokemon Name", "Type"]
x.add_row(["Pikachu", "Electric"])
x.add_row(["Squirtle", "Water"])
x.add_row(["Charmander", "Fire"])


x.align = "l"

print (x)