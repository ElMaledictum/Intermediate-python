from tkinter import *
from quiz_logic import QuizLogic
from tkinter import messagebox
THEME_COLOR = "#fff1ce"
WINDOW_COLOR = "#139487"
CORRECT_COLOR = "#357c3c"
WRONG_COLOR = "#ef6d6d"


class QuizUi:
    def __init__(self, quiz_logic:QuizLogic):
        self.quiz = quiz_logic
                
        self.win = Tk()
        self.win.title("Take a Quiz")
        self.win.config(padx=20, pady=20, bg=WINDOW_COLOR)

        self.score_label = Label(text=f"Score: 0",
            fg="black",
            padx=30, pady=30, 
            bg=WINDOW_COLOR, 
            font=("Ubuntu", 13, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(
            width=300, 
            height=250, bg=THEME_COLOR, 
            highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150, 
            120, 
            width=280,
            text=f"Put Question here", 
            font=("Ubuntu", 20, "italic"))

        f_image = PhotoImage(file="./images/false.png")
        self.f_button = Button(
            image=f_image, 
            highlightthickness=0,
            command=self.answer_is_false
            )
        self.f_button.grid(column=1, row=2)

        t_image = PhotoImage(file="./images/true.png")
        self.t_button = Button(
            image=t_image, 
            highlightthickness=0,
            command=self.answer_is_true
            )
        self.t_button.grid(column=0, row=2)
        
        self.get_next_question()

        self.win.mainloop()

    def answer_is_true(self):
        is_correct = self.quiz.is_correct("True")
        self.add_feedback(is_correct)


    def answer_is_false(self):
        is_correct = self.quiz.is_correct("False")
        self.add_feedback(is_correct)

   
    def get_next_question(self):
        self.t_button.config(state="active")
        self.f_button.config(state="active")
        self.canvas.config(bg=THEME_COLOR)
        if self.quiz.still_has_questions():   
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end!")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")
            percentage = round((self.quiz.score/self.quiz.total_questions) * 100)
            messagebox.showinfo(
                title="Quiz ended!", 
                message=f"Total score: {self.quiz.score}/{self.quiz.total_questions} or \
                                     {percentage}%"
                )

    def add_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg=CORRECT_COLOR)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg=WRONG_COLOR)
        self.t_button.config(state="disabled")
        self.f_button.config(state="disabled")
        self.change_color_timer = self.win.after(1000, self.get_next_question)
