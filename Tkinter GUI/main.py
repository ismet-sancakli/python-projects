from tkinter import *
# The reason we add the library like this,without tkinter prefix to access the classes directly.
import random


window = Tk() # window is an object.
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) # Padding as CSS
# Label

my_label = Label(text="I am label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)  # pack method for the screen placement.Default is center.

my_label["text"] = "New text" # This script has changed "I am label".
my_label.config(text="Label") # And then new writing has configured.


# Button


def button_clicked():
    print("I got clicked")
    new_text = any_input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked) # Command is here to call the function, without brackets.
button.grid(column=1, row=1)


# New Button

new_button = Button(text="new button")
new_button.grid(column=2, row=0)


# Entry

any_input = Entry(width=25, bg="grey")
any_input.grid(column=3, row=3)
any_input.get() # Returns the entry's string.


window.mainloop() # mainloop yaptıklarımızın çıktısını almamız için temel yapı.

""""
Tkinter layout 

1-pack(): Actually this isn't efficiency. Because it always do alignment top to end (for default.) side=left/right etc.
2-place(): x and y coordinates are used. for instance x=100 , y=150 etc.
3-grid(): Grid is the best way for the placement.The window is divided into equal parts like this matrix with grid system.
Grid uses column and row.

These layouts are incompatible each other.
"""

