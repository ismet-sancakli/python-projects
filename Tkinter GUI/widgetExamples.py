from tkinter import *

window = Tk()
window.title("Widget Example")
window.minsize(height=500, width=500)

# Labels

label = Label(text="This is old text.")
label.config(text="This is new text.")
label.pack()


# Button


def action():
    print("Do something")


button = Button(text="Click Me", command=action)
button.pack()

# Entries

entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Something")
# Gets text entry
print(entry.get())
entry.pack()

# Text

text = Text(width=30, height=5)
# Puts cursor in textbox
text.focus()
# Add some text to begin with
text.insert(END, "Can you add anything")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END)) # 1.0 means: Text starting from the 1 line with 0 character.
text.pack()

# Spinbox


def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=15, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, width=20, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar() # IntVar is a class, it has int value.
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()



# Radiobutton


def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4, bg="grey")
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
