from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
from walls import Walls
import time
import os
os.system("cls")


scr = Screen()
scr.setup(width=600, height=600) #but playable is only 580, 580, 580, 570
scr.bgcolor("black")
scr.title("Snake")
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
walls = Walls()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

is_gaming = True
while is_gaming:
    scr.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision of snake and food
    if snake.snakehead.distance(food) < 8:
        food.refresh_location()
        scoreboard.add_score()
        #grow 2 lengths of snake
        for x in range(5):
            snake.grow()

    
    #Detect collision with wall
    xcoor = snake.snakehead.xcor()
    ycoor = snake.snakehead.ycor()
    if xcoor > 275 or xcoor < -275 or ycoor > 280 or ycoor < -278:
        # print ("Collided with wall!")
        scoreboard.game_over()  
        snake.reset() 
        # break 

    #detect colision with the body of the snake
    for each_part in snake.body[1:]:
        if snake.snakehead.distance(each_part) < 4:
            scoreboard.game_over()
            snake.reset() 

            # is_gaming = False

scr.exitonclick()

