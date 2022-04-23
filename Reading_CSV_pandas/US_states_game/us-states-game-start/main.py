from turtle import Turtle, Screen
import os
import pandas as pd
os.system("cls")

screen = Screen()
screen.title("U.S. States Game")
screen.screensize(canvwidth=491, canvheight=725)
image = "blank_states_img.gif"
screen.addshape(image)

t = Turtle()
t.shape(image)
state_name = Turtle()
state_name.penup()
state_name.hideturtle()
    

data = pd.read_csv("50_states.csv")
state_list = data.state.to_list()

def location(answer):
    global data
    row = data[data.state == answer.title()] #get the row where the state == answer 
    x = int(row.x)
    y = int(row.y)
    return (x ,y)

guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(f"{len(guessed_states)}/50 | Guess the state",
     "What's the state name? ").title()

    if user_answer == "Exit":
        #generate states_to_learn.csv
        missing_states = [item for item in state_list if item not in guessed_states]
        new_data = pd.DataFrame(missing_states)        
        new_data.to_csv("states_to_learn.csv")
        break

    elif user_answer in state_list and user_answer not in guessed_states:
        # print (location(user_answer))
        state_name.goto(location(user_answer))
        state_name.write(user_answer)
        guessed_states.append(user_answer)

