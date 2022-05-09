from tkinter import *
import os
os.system('cls')

WORK_CYCLE = [25, 5, 25, 5, 25, 5, 20]
# WORK_CYCLE = [1, 2, 1, 2, 1, 2, 1, 5]
FONT_NAME = "Ubuntu"
PALETTE = ["#6FB2D2", "#85C88A", "#EBD671", "#42C2FF"]
TIMER_COLOR = ["#1b1a17", "#f0a500", "#e45826", "#e6d5b8"]
check = "✔"
reps = -1
t = None


def start_timer():
    global reps
    if reps > len(WORK_CYCLE)-1:
        reps = -1
    reps += 1

    if reps == 7:
        count_down(WORK_CYCLE[-1]-1)
        print(reps, "long break")
        win.title("LONG BREAK")

    elif reps % 2 == 1:
        print(reps, "break")
        win.title("BREAK")

    elif reps % 2 == 0:
        print(reps, "work 25")
        win.title("WORK")

    count_down(WORK_CYCLE[reps]-1)


def change_gui():
    global i
    if i == len(PALETTE)-1:
        i = -1
    i += 1
    canvas.itemconfig(timer, fill=TIMER_COLOR[i])
    canvas.itemconfig(timer_image, image=pause_img)
    canvas.configure(bg=PALETTE[i])
    if reps in range(0, 9, 2):
        check_marks[reps].place(x=50, y=y)


def reset_timer():
    global t, reps
    canvas.itemconfig(timer, text=f"25:00")
    win.after_cancel(t)
    reps = -1

def count_down(minute, second=59):
    global y, reps, t
    # edits the text in the canvas to countdown
    canvas.itemconfig(timer, text=f"{minute}:{second}")
    if minute < 0:
        start_timer()
        change_gui()
        y += 15

    if minute >= 0:
        if second < 10:
            # edits the text in the canvas to countdown
            canvas.itemconfig(timer, text=f"{minute}:0{second}")
            if minute < 10:
                # edits the text in the canvas to countdown
                canvas.itemconfig(timer, text=f"0{minute}:0{second}")
        elif minute < 10:
            # edits the text in the canvas to countdown
            canvas.itemconfig(timer, text=f"0{minute}:{second}")
        if second <= 0:
            second = 10  # reset second to 59 if second equals to zero
            minute -= 1

        second -= 1
        # waits 1sec then pass t-1 to count_down to loop again
        t= win.after(1000, count_down, minute, second)


i = 0
win = Tk()
win.title("Pomodoro!", )
win.geometry("300x300")


canvas = Canvas(win, width=300, height=300, bg=PALETTE[i])
play_img = PhotoImage(file="play_resized2.png")
pause_img = PhotoImage(file="pause_resized2.png")

timer_image = canvas.create_image(150, 150, image=play_img)
timer = canvas.create_text(
    160, 150, fill=TIMER_COLOR[i], text="25:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


y = 90
start_but = Button(text="START", font=(FONT_NAME, 8, "bold"),
                   fg=PALETTE[i], width=6, command=start_timer, highlightthickness=0)
reset_but = Button(text="RESET", font=(FONT_NAME, 8, "bold"),
                   fg=PALETTE[i], width=6, command=reset_timer, highlightthickness=0)
start_but.place(x=130, y=35)
reset_but.place(x=130, y=240)

check_marks = [Label(text=check, bg="yellow") for _ in range(8)]
# check_marks[reps].place(x=50, y=y)


win.mainloop()
