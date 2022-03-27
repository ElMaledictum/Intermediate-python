from turtle import Turtle, Screen
from os import system
from random import randint
import turtle
system("cls")

t = Turtle()
screen = Screen()

t.shape("arrow")
t.color("blue", "black")
t.speed(3)
turtle.colormode(255)
t.pensize(2)


def randomize_pencolor():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


def draw_shape(radius, sides):
    t.penup()
    t.sety(-radius)
    t.pendown()

    t.circle(radius, steps=sides)


def main():
    rad = 100
    for sides in range(3,5):
        t.pencolor(randomize_pencolor())
        draw_shape(rad, sides)

        t.penup()
        t.home()
        
        rad += 10

main()
    
 
























screen.exitonclick()
# screen.bye()
