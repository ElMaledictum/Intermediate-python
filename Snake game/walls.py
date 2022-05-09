from turtle import Turtle


class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.pensize(3)
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=290)
        self.pendown()
        self.setheading(270)

        self.create_walls()

    def create_walls(self):
        for _ in range(3):
            self.forward(570)
            self.left(90)
        c = 0
        while c < 2:
            self.setheading(180)
            self.forward(210)
            if c == 0:
                self.left(90)
                self.forward(10)
                self.right(90)
                self.forward(150)
                self.right(90)
                self.forward(10)
            c += 1
