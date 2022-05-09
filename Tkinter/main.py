from tkinter import *
import os
from entries import Distance, DistanceLabel
os.system('cls')


window = Tk()
window.title("Miles to Km")
window.geometry("300x200")
window.config(padx=10, pady=30)


def convert():
    k = k_entry.get()
    m = m_entry.get()

    if k :
        m = round(int(k) * 0.62137)
        m_entry.delete(0, END)
        m_entry.insert(0, str(m))
    if m:
        k = round(int(m) * 1.609344)        
        k_entry.delete(0, END)
        k_entry.insert(0, str(k))

    return None

def click_entry(event):
    m_entry.configure(state=NORMAL)
    m_entry.delete(0, END)
    m_entry.insert(0, "")
    k_entry.configure(state=NORMAL)
    k_entry.delete(0, END)
    k_entry.insert(0, "")


convert_label = Label(window, text="Convert to: ", font=("Arial", 10, ("italic", "bold")))
convert_label.grid(column=0, row=1)

m_entry = Distance(window, "0", 1, 0)
k_entry = Distance(window, "0", 1, 2)
k_entry.bind("<Button-1>", click_entry)
m_entry.bind("<Button-1>", click_entry)



k_label = DistanceLabel(window, "kilometers", 2, 2)
m_label = DistanceLabel(window, "miles", 2,0)


calc_button = Button(text="Convert", width=5, command=convert) 
calc_button.grid(column=1, row=4)
calc_button.config(padx=5, pady=5)


window.mainloop()
    