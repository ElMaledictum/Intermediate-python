from turtle import Turtle

SCORE_FONT = ("Courier", 20, "bold")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-290, 260)
        self.lvl = 1
        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.write(arg=f"Level:{self.lvl}", align="left", font=SCORE_FONT)

    def add_level(self):
        self.lvl += 1
        #clear all written level then add level
        self.clear()
        self.update_level()
    
    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER!", align="center", font=SCORE_FONT)
