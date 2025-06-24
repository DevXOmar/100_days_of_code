import tkinter as tk
from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#ca8187"
RED = "#e7305b"
GREEN = "#75d18c"
YELLOW = "#f7f5dd"
BLUE = "#02075d"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(timer)
    label1.config(text="TIMER", fg = GREEN)
    REPS = 0
    canvas1.itemconfig(timer_text, text=f"00:00")
    label2.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(x):
    global timer
    print(x)
    mins = x // 60
    sec = x - (60*mins)

    if sec < 10:
        sec = f"0{sec}"## Dynamic conversion
    if sec == 0:
        sec = "00"##
    if mins < 10:
        mins = f"0{mins}"

    canvas1.itemconfig(timer_text,text = f"{mins}:{sec}")
    if x > 0 :
       # window.after(1000,count_down,x-1) ##
       timer = window.after(1000,count_down,x-1)
    else:
        start_timer()## Triggered when time < 0, calls start_timer again.
        mark = ""
        work_sessions = REPS//2
        for x in range (work_sessions):
            mark += "✔"
            label2.config(text=mark)
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label1.config(text = "BREAK", fg = RED)
        # label2.config(text="✔")

    elif REPS % 2 == 1 :
       count_down(WORK_MIN*60)
       label1.config(text="WORK TIME",fg = BLUE)
       # label2.config(text="")
    elif REPS % 2 != 1:
        count_down(SHORT_BREAK_MIN*60)
        label1.config(text="BREAK",fg = PINK)
        # label2.config(text="✔")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
# window.minsize(500,300)
window.config(padx = 80, pady = 50, bg = YELLOW)



#canvas
canvas1 = tk.Canvas(width = 210, height = 225, bg = YELLOW, highlightthickness = 0)
img1 = PhotoImage(file = "tomato.png")
canvas1.create_image(103,112,image = img1)
timer_text = canvas1.create_text(103,125,text = "00:00", fill = "white", font = (FONT_NAME,32,"bold"))
canvas1.grid(row = 2,column = 2)

#label
label1 = tk.Label(text = "Timer",font = (FONT_NAME,40,"bold"), bg = YELLOW, fg = GREEN)
label1.grid(row = 1,column = 2)



label2 = tk.Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME,32,"bold"))
label2.grid(row = 3, column = 2)

#button

button1 = tk.Button(text = "Start",bg = YELLOW, highlightbackground= YELLOW, command = start_timer)
button1.grid(row = 3,column = 1)

button2 = tk.Button(text = "Reset",bg = YELLOW, highlightbackground = YELLOW, command = reset_timer)
button2.grid(row = 3,column = 3)



window.mainloop()


