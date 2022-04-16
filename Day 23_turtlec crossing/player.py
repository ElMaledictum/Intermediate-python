from turtle import Turtle

INITIAL_POSITION = (0, -270)
MOVEMENT_SPEED = 15

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        self.forward(MOVEMENT_SPEED)

    def reset_position(self):
        self.goto(INITIAL_POSITION)
