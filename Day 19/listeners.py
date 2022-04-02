from turtle import Turtle, Screen
import os
os.system('cls')

t = Turtle()
s = Screen()
t.pensize(3) 

def move_forward():
    t.forward(10)

def move_backward():
    new_head = t.heading() + 180
    t.setheading(new_head)
    
def ccw():
    new_head = t.heading()
    new_head += 10
    t.setheading(new_head)

def cw():
    new_head = t.heading()
    new_head -= 10
    t.setheading(new_head)

def erase_drawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()





s.listen()

s.onkeypress(move_forward, "w")
s.onkeypress(move_backward, "s")
s.onkeypress(ccw, "a")
s.onkeypress(cw, "d")
s.onkeypress(erase_drawing, "c")

s.exitonclick()

