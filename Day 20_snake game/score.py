from turtle import Turtle

SCORE_FONT = ("Courier", 13, "bold")
LOSE_FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align="center", font=SCORE_FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER!", align="center", font=LOSE_FONT)
