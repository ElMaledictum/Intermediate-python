from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(2)
        self.penup()
        self.create_walls()
        self.mid_wall()


    def create_walls(self):
        self.goto(-390, -280) #(x,y)
        self.pendown()
        for _ in range(2):
            self.pencolor("red")
            self.forward(770)
            self.left(90)
            self.pencolor("blue")
            self.forward(570)
            self.left(90)

    def mid_wall(self):
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        self.pencolor("orange")
        for _ in range(0, 285, 5):
            self.penup()
            self.forward(5)
            self.pendown()
            self.forward(5)
