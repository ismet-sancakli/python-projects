from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
s_count = 0


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    time_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
    check_mark_label.config(bg=YELLOW)
    global reps
    reps = 0
    global s_count
    s_count = 0


def start_timer():
    global s_count
    s_count += 1
    if s_count == 1:
        global reps
        reps += 1

        work_sec = WORK_MIN * 60
        short_break = SHORT_BREAK_MIN * 60
        long_break = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break)
            time_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break)
            time_label.config(text="Break", fg=PINK)
        else:
            count_down(work_sec)
            time_label.config(text="Work", fg=GREEN)



def count_down(count):

    count_min = math.floor(count / 60) # math.floor() method rounds a number down the nearest int.
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00" # This is due to the python dynamic structure. int to str or vice versa.
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer() # For the break or another working section.
        marks = ""
        working_sessions = math.floor(reps/2)
        for _ in range(working_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)


"""
The after() method calls the callback function once after a delay milliseconds (ms) within Tkinter main loop.
"""


window = Tk()
window.title("Pomodoro Working Technique")
window.config(padx=100, pady=50, bg=YELLOW)

time_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold")) # fg for the writing color.
time_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") # Firstly we got the file path.
canvas.create_image(100, 112, image=tomato_img) # x,y coordinates are 103,112, we've tweaked our image.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_label = Label(bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)
window.mainloop()



