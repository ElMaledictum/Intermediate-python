from tkinter import *
from tkinter import ttk
# image = PhotoImage(file="button.png")

LABEL_FONT = ("Ubuntu", 11, "bold")
class InputLabels(Label):
    def __init__(self, master, string, x, y):
        super().__init__(master, pady=10, text=string, font=LABEL_FONT, justify="center",
            bg="#143f6b", fg="#fffbe7", height=1)
        
        self.place(x=x, y=y)

# columnspan=2 (using entry.grid(columnspan=2)) is another attribute of the input entry
class Input(Entry):
    def __init__(self, master, width, x, y):
        super().__init__(master, width=width, justify=CENTER,
        font=("Ubuntu", 8, "bold"))
        self.place(x=x, y=y)

class GenerateButton(Button):
    def __init__(self, master, text, width, height, x, y, func):
        super().__init__(master=master, width=width, bg="#f55353",
        highlightthickness=0, borderwidth=0, text=text, relief="groove", 
        foreground="black", height=height, bd=0, command=func)

        self.place(x=x, y=y)