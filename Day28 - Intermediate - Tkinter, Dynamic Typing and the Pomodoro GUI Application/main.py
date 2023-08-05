from tkinter import Tk, Canvas, PhotoImage, Label, Button
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps, check
    reps = 0
    window.after_cancel(count_timer)
    canvas.itemconfig(timer_display, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    check =  ""
    check_marks.config(text=check)
    print("reset successfully")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer.config(text="Long Break", fg=PINK)
        start_countdown(long_break)
        
    elif reps % 2 == 0:
        timer.config(text="Short Break", fg=PINK)
        start_countdown(short_break)
    else:
        timer.config(text="Work", fg=GREEN)
        start_countdown(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def start_countdown(count):
    global check, check_marks
    minutes = math.floor(count / 60)
    seconds = count % 60


    if len(str(minutes)) == 1:
        minutes = str(f"0{minutes}")
    if len(str(seconds)) == 1:
        seconds = str(f"0{seconds}")

    canvas.itemconfig(timer_display, text=f"{minutes}:{seconds}")
    if count > 0:
        global count_timer

        count_timer = window.after(1000, start_countdown, count - 1)
    else:
        start_timer()

        if reps % 2 == 0:
            check += "✔"
            check_marks.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=100, bg=YELLOW)

timer = Label(text="Timer")
timer.config(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_display = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill="white")
canvas.grid(column=1, row=1)

check = ""
check_marks = Label(text="")
check_marks.config(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW, pady=30)
check_marks.grid(column=1, row=4)

start_button = Button(text="Start", command=start_timer)
start_button.config(bg=GREEN, fg="black", font=(FONT_NAME, 10, "bold"), borderwidth=0, width=8, height=2)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.config(bg=PINK, fg="black", font=(FONT_NAME, 10, "bold"), borderwidth=0, width=8,  height=2)
reset_button.grid(column=3, row=2)


window.mainloop()