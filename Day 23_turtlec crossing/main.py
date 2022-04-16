from turtle import Screen
from player import Player
from level import Level
from car import Car
import os
import time

os.system("cls")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.colormode(255)

player = Player()
level = Level()
car = Car()

screen.onkeypress(player.move_up, "Up")

is_gaming = True
counter = 0
while is_gaming:
    time.sleep(0.05)
    screen.update()
    car.move_left()

    car.generate_car()

    #check if the player successfully crossed the street
    if player.ycor() > 290:
        player.reset_position()
        level.add_level()
        car.add_speed()

    #detect car-player collision
    for each_car in car.all_cars:
        if player.distance(each_car) < 24:
            level.game_over()
            is_gaming = False

    counter += 1



screen.exitonclick()

