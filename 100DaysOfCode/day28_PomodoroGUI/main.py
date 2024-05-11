from tkinter import *
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
pause = False
timer = None

# ---------------------------- TIMER PAUSE ------------------------------- #


def pause_timer():
    global pause
    if pause:
        pause = False
        pause_button.config(text="Pause")
    else:
        pause = True
        pause_button.config(text="Resume")

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_time():
    window.after_cancel(timer)
    canvas.itemconfigure(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if not reps % 8:
        countdown(long_break)
        timer_label.config(text="Break", fg=RED)
    elif not reps % 2:
        countdown(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_secs)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(time):
    global pause
    minutes = time // 60
    seconds = time % 60
    checks = 0
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfigure(timer_text, text=f"{minutes}:{seconds}")
    if time > 0:
        global timer
        if not pause:
            timer = window.after(1000, countdown, time - 1)
        else:
            timer = window.after(1000, countdown, time)
    else:
        start_timer()
        if not reps % 2:
            checks = reps // 2
            check.config(text="✓"*checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Add background image to screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Add Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

# Start button
start = Button(text="Start", bg="white", font=("Arial", 10, "bold"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# Reset button
reset = Button(text="Reset", bg="white", font=("Arial", 10, "bold"), highlightthickness=0, command=reset_time)
reset.grid(column=2, row=2)

# Pause button
pause_button = Button(text="Pause", bg="white", font=("Arial", 10, "bold"), highlightthickness=0, command=pause_timer)
pause_button.grid(column=1, row=4)

# Check Label
check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check.grid(column=1, row=3)


window.mainloop()
