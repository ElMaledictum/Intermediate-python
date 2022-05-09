from tkinter import *
from tkinter import messagebox
import pandas
import random
import time
import os
os.system("clear" or "cls")

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

data_dict = data.to_dict(orient="records")
current_card = {}

execute
def generate_card():
    global current_card, flip_timer
    win.after_cancel(flip_timer)
    if len(data_dict) ==0:
        messagebox.showinfo(title="Prompt", message="No more words.")
    else:
        current_card = random.choice(data_dict)
        french_word = current_card["French"]
        canvas.itemconfig(canvas_image, image=pic_front)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=french_word, fill="black")
        print (french_word, len(data_dict))
        flip_timer = win.after(3000, flip_card)

def flip_card():
    eng_word = current_card["English"]    
    canvas.itemconfig(canvas_image, image=pic_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=eng_word, fill="white")


def is_known():
    global data_dict
    data_dict.remove(current_card)
    known_words = pandas.DataFrame(data_dict)
    known_words.to_csv("./data/words_to_learn.csv", index=False)
    generate_card()


win = Tk()
# win.geometry("900x700")
win.title("Flash Card")
win.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = win.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
pic_front  = PhotoImage(file="./images/card_front.png")
pic_back = PhotoImage(file="./images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=pic_front)

card_title = canvas.create_text(400, 150, text="French", font=("Source Code Pro", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Source Code Pro", 50, "bold"))

canvas.configure(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)


correct_pic = PhotoImage(file="./images/right.png")
correct_button = Button(padx=50, pady=50, image=correct_pic, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=1)

wrong_pic = PhotoImage(file="./images/wrong.png")
wrong_button = Button(padx=50, pady=50, image=wrong_pic, highlightthickness=0, command=generate_card)
wrong_button.grid(row=1, column=0)

generate_card()

win.mainloop()


