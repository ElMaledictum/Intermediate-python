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
        
        with open("E:\Python_programs\Intermediate-python\Day 20_snake game\data.txt", "r") as file:
            x = file.read()
            x.strip()
            self.high_score = int(x)

        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}|High Score: {self.high_score}", align="center", font=SCORE_FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("E:\Python_programs\Intermediate-python\Day 20_snake game\data.txt", "w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_score()