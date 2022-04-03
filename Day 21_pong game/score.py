from turtle import Turtle

SCORE_FONT = ("Courier", 50, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.rscore = 0
        self.lscore = 0
        self.goto(0, 200)

        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f"{self.lscore}    {self.rscore}", align="center", font=SCORE_FONT)

    def add_score(self, paddle):
        if paddle == 'l':
            self.lscore += 1
        else:
            self.rscore += 1
        self.clear()
        self.update_score()
    
    def game_over(self, string):
        self.goto(0, 0)
        if string == "l":
            self.write(arg="Left player wins!", align="center", font=SCORE_FONT)
        elif self.rscore == 5:
            self.write(arg="Right player wins!", align="center", font=("Courier", 30, "bold"))

