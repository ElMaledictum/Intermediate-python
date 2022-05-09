from turtle import Screen
from paddle import Paddle
from ball import Ball
from walls import Wall
from score import ScoreBoard
import os
import time

os.system("cls")

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

r_paddle = Paddle(370, 0)
l_paddle = Paddle(-380, 0)
ball = Ball()
wall = Wall()
scores = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up" )
screen.onkeypress(r_paddle.down, "Down" )
screen.onkeypress(l_paddle.up, "w" )
screen.onkeypress(l_paddle.down, "s" )

def collided(paddle):
    if ball.distance(paddle) < 60 and ball.xcor()>360:
        return True
    elif ball.distance(paddle) < 60 and ball.xcor()<-360:
        return True
    
is_gaming = True
while is_gaming:
    time.sleep(ball.frame_spd)

    screen.update()
    ball.move()

    #detect collision with walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce(ball.heading())

    #detect collision with paddles
    elif collided(l_paddle) or collided(r_paddle):
        ball.reflect(ball.heading())
        
    elif ball.xcor() > 380:
        #right paddle score+= 1
        scores.add_score("l")
        ball.reset_pos()

    elif ball.xcor() < -380:
        #left paddle score+= 1
        scores.add_score("r")
        ball.reset_pos()

        if scores.lscore == 5:
            scores.game_over("l")
            is_gaming = False

        elif scores.rscore == 5:
            scores.game_over("r")
            is_gaming = False




screen.exitonclick()