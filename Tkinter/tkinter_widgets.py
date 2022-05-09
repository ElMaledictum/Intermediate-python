from tkinter import *
#LABEL
label = Label(text="This is a label", font=("Cambria", 24, "bold"))
label.pack()

#BUTTONS
def clicked():
    print ("I got clicked!")
    label.config(text=entry.get())
    print (entry.get())


button = Button(text="Click me!", command=clicked)
button.pack(pady=10)

#ENTRY
def delete_contents(event):
    entry.configure(state=NORMAL)
    entry.delete(0, END)
    entry.unbind("<Button-1>")


entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Enter your name here.")
#Gets text in entry
entry.pack()  

entry.bind("<Button-1>", delete_contents)



# #Text
text = Text(height=5, width=30, font=("Cambria", 11, "italic"))
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(1.0, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get(1.0, END)) #prints the whole text from char 0 to END
text.pack()




#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()



#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

