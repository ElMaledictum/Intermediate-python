from turtle import Turtle
import random
import time

BALL_SPEED = 7
ANGLES = [angle for angle in range(30, 330, 45)]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(3)
        self.frame_spd = 0.09
        self.random_heading()


    def random_heading(self):
        self.setheading(random.choice(ANGLES))
    
    def move(self):
        self.forward(BALL_SPEED)

    def bounce(self, heading_before):
        new_heading = 360 - heading_before
        self.setheading(new_heading)

    def reflect(self, heading_before):
        new_heading = 180 - heading_before
        self.setheading(new_heading)
        self.frame_spd *= 0.7

    def reset_pos(self):
        time.sleep(0.1)
        self.goto(0, 0)
        time.sleep(0.1)
        self.frame_spd = 0.1
        self.reflect(self.heading())