from tkinter import *
from tkinter import messagebox
from labels import InputLabels, Input, GenerateButton
from random import randint
import json
import os
os.system("clear" or "cls")


def generate_password():
    password = ""
    # unicode numbers 33-126
    for i in range(16):
        char = chr(randint(33, 126))
        password += char

    pword.delete(0, END)
    pword.insert(0, password)
    # automatically copy the generated pass word to clipboard
    win.clipboard_clear()
    win.clipboard_append(password)
    return password


def save_to_file():
    def ask():
        entered_pass = pword.get()
        entered_site = site.get()
        entered_name = name.get()
        new_data = {
            entered_site: {
                "email": entered_name,
                "password": entered_pass
            },
        }

        is_ok = messagebox.askokcancel(title=site.get(
        ), message=f"Details entered:\n\nEmail: {name.get()}\nPassword: {pword.get()}\n\nIs it ok to save? ")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                print(f"Created a new file.")
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except:  # if empty json file
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            pword.delete(0, END)
            site.delete(0, END)

    if not pword.get() or not site.get() or not name.get():
        messagebox.showinfo(title="Missing", message="Missing fields!")
    else:
        ask()


def search():
    entered_site = site.get()
    with open("data.json", "r") as file:
        curr_data = json.load(file)
        try:
            email_data = curr_data[entered_site]["email"]
        except KeyError:
            messagebox.showinfo(title="Search results",
                                message=f"No data found on {entered_site}")
        else:
            password_data = curr_data[entered_site]["password"]
            messagebox.showinfo(
                title="Search results", message=f"Email: {email_data}\nPassword: {password_data}")
            pword.delete(0, END)
            pword.insert(0, password_data)
            name.delete(0, END)
            name.insert(0, email_data)


win = Tk()
win.title("Password Manager")
win.geometry("700x440")
win.attributes('-alpha', 0.99)


canvas = Canvas(win, width=700, height=470)
image = PhotoImage(file="logo_small.png")
canvas.create_image(350, 225, image=image)
canvas.place(x=0, y=0)

canvas2 = Canvas(win, width=340, height=400,
                 bg="#143f6b", highlightthickness=0)
canvas2.place(x=15, y=22)


site_label = InputLabels(win, "Website:", 25, 100)
username_label = InputLabels(win,
                             """Email/
  Username:""", 20, 140)
pword_label = InputLabels(win, "Password:", 25, 185)

site = Input(win, 20, 120, 115)
site.focus()
name = Input(win, 37, 120, 155)
name.insert(0, "cyrus@email.com")
pword = Input(win, 37, 120, 198)


generate_button = GenerateButton(
    win, "Generate Random Password", 25, 0, 140, 225, generate_password)

save_button = GenerateButton(win, "Save", 30, 3, 120, 275, save_to_file)
search_button = GenerateButton(
    win, "Search data of Site", 14, 1, 250, 110, search)


win.mainloop()
