import math
from tkinter import *
# ---------------------------- CONSTANTS -------------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps=0
timer= None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer_txt.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_start_timer():
    global reps
    if reps==0:
        start_timer()
def start_timer():
    global reps
    reps+= 1
    if reps%8 == 0:
        count_down(LONG_BREAK_MIN)
        Timer_txt.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN)
        Timer_txt.config(text="Break",fg=PINK)
    else:
        count_down(WORK_MIN)
        Timer_txt.config(text="Work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    min= math.floor(count/60)
    sec= count%60
    if sec < 10:
        sec=f"0{sec}"
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for i in range(work_session):
            mark+="🗸"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=20,padx=20,bg=YELLOW)

Timer_txt = Label(text="TIMER",fg=GREEN,bg=YELLOW ,font=(FONT_NAME,55))
Timer_txt.grid(column=1,row=0)


canvas = Canvas(width=250,height=250,bg=YELLOW,highlightthickness=0)
toma = PhotoImage(file="tomato.png")
canvas.create_image(125,125,image=toma)
timer_text = canvas.create_text(125,140,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



#button
start = Button(text="Start",highlightthickness=0,command=start_start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2, row=2)

#tick
tick = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
tick.grid(column=1,row=3)


window.mainloop()