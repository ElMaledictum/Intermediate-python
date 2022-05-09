from turtle import Turtle

PADDLE_SPEED = 30
class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=0.5)#paddle size w = 10, l = 100 l/2 = 50
        self.penup()
        self.goto(xcor, ycor)

    def up(self):
        if self.ycor() < 215:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)
        
    def down(self):
        if self.ycor() > -206:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)
        
