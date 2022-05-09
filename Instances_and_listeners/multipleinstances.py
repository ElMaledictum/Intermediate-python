from turtle import Turtle, Screen, color
import os
import random
os.system('cls')
#make 5 turtles
s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title = "Who's your bet?", prompt="Enter color ")


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet'] #6 turtles
turt_list = []
ycor = -120
for t_index in range(0, 6):
    t = Turtle(shape="circle")
    t.color(colors[t_index])
    t.penup()
    t.goto(x=-230, y=ycor)
    ycor += 50
    turt_list.append(t)

# print (turt_list)
is_still_running = True

if user_bet:
    while is_still_running:
        for i in range(len(turt_list)):  
            if turt_list[i].xcor() >= 200:
                print ("Race finished!")
                win_color = turt_list[i].pencolor()
                s.bgcolor(win_color)
                is_still_running = False
    
            distance = random.randint(0, 10)
            turt_list[i].forward(distance)

print (f"The winner is Turtle {win_color} at {turt_list[i].xcor()}")
if user_bet == win_color:
    print ("You win!")

else:
    print ("You lose!")

s.exitonclick()