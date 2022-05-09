from tkinter import *

LABEL_FONT = ("Ubuntu", 13, "bold")
class Distance(Entry):
    def __init__(self, master, place_holder, col, row):
        super().__init__(master, width=10, justify=CENTER)

        self.insert(0, string=place_holder)
        self.grid(column=col, row=row)

class DistanceLabel(Label):
    def __init__(self, master, string, col, row):
        super().__init__(master, pady=10, text=string, font=LABEL_FONT, justify="left")
        
        self.grid(column=col, row=row)

