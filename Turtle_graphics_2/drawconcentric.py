from turtle import Turtle, Screen
t = Turtle()

def draw_shape(radius, sides):

    # move start point

    t.penup()

    t.sety(-radius)

    t.pendown()

    # draw "almost" circle

    t.circle(radius, steps=sides)

radius = 100
sides = 4

for shape in range(1):
    draw_shape(radius, sides)
    t.penup()
    t.home()
    # t.pendown()

screen = Screen()
screen.exitonclick()