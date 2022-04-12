# Imports:
import os.path
import subprocess
import sys
import time
import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Begin "loop" of interface:
import callback

root = tk.Tk()
root.title('FETT - Focus Enhancement and Tracking Tool')
root.iconbitmap('media/fet.ico')

# Designate height and width of app:
appWidth = 1600
appHeight = 900

# Get screen width and height:
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

# Create x and y coordinates for window centering:
x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)

# Formulae for centering window:
root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

# Notebook init:
notebook = ttk.Notebook(root)
notebook.pack(pady=15)

global temp, secs


# Go to Statistics tab function:
def select():
    notebook.select(1)


# Creating tabs:
frame1 = Frame(notebook, width=screenWidth, height=screenHeight, bg="#707c74")
frame2 = Frame(notebook, width=screenWidth, height=screenHeight, bg="white")

# Packing tabs:
frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)

# Adding tabs, allowing functionality and title:
notebook.add(frame1, text="Timer")
notebook.add(frame2, text="Statistics")

# Setting up fonts:
# buttonFont1 = font.Font(family = 'Helvetica', size = 12, weight= 'bold')
buttonFont2 = font.Font(family='Helvetica', size=10)
timerFont1 = font.Font(family='Calibri', size=40, weight='bold')

# Setting images for buttons and labels:
Start_btn = PhotoImage(file='media/Start_btn.png')
Stop_btn = PhotoImage(file='media/Stop_btn.png')
ThirtyMins_btn = PhotoImage(file='media/30mins_btn.png')
OneHour_btn = PhotoImage(file='media/1hour_btn.png')
Pomodoro_btn = PhotoImage(file='media/Pomodoro_btn.png')
Custom_btn = PhotoImage(file='media/Custom_btn.png')
Base = PhotoImage(file='media/base.png')
Exit_btn = PhotoImage(file='media/exit_btn.png')

# Blank Labels:
blankLabel1 = Label(frame1, text="        ", font=timerFont1, fg="#707c74", bg="#707c74").grid(row=1, column=1)
blankLabel2 = Label(frame1, text="        ", font=timerFont1, fg="#707c74", bg="#707c74").grid(row=2, column=1)
blankLabel2 = Label(frame1, text="        ", font=timerFont1, fg="#707c74", bg="#707c74").grid(row=6, column=1)


# Adding Timer Base:
TimerBase = Label(frame1, image=Base, bg='#707c74').grid(row=3, column=3, columnspan=2, rowspan=1, padx=10, pady=40)

# Timer Label:
timer = Label(frame1, text=":", font=timerFont1, fg='White', bg='#3b3838').grid(row=3, column=3, columnspan=2,
                                                                                rowspan=1, padx=10, pady=40)
root.bind('<Return>', callback)

# Assigning variables:
minute = StringVar()
minute.set("00")
second = StringVar()
second.set("00")

# Inputs:
minuteEntry = Entry(frame1, width=2, font=timerFont1, textvariable=minute, fg="white", bg="#3b3838",
                    borderwidth=0).grid(row=3, column=3, sticky="E", padx=15)
secondEntry = Entry(frame1, width=2, font=timerFont1, textvariable=second, fg="white", bg="#3b3838",
                    borderwidth=0).grid(row=3, column=4, sticky="W", padx=15)


# Start function
def start1():
    global temp
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:

        # divmod(first value = temp//60, second value = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs
        # mins ,secs(input = 110 min --> 120*60 = 6600:
        # 50min: 0sec)
        if mins > 60:
            # divmod(first value = temp//60, second value
            # = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to
        # two decimal places
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
            minute.set("00")
            second.set("00")

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1


# Stop function:
def stop():
    os.execl(sys.executable, sys.executable, *sys.argv)

# Exit function:
def exit():
    root.destroy()


# Adding tab1 buttons:
startButton = Button(frame1, image=Start_btn, borderwidth=0, command=start1, bg="#707c74", highlightthickness=0, bd=0).grid(row=3, column=2, padx=10, pady=10)
stopButton = Button(frame1, image=Stop_btn, borderwidth=0, command=stop, bg="#707c74", highlightthickness=0, bd=0).grid(row=3, column=5, padx=10, pady=10)

ThirtyMinsButton = Button(frame1, image=ThirtyMins_btn, bg="#707c74", highlightthickness=0, bd=0).grid(row=5, column=2, padx=10, pady=10)
OneHourButton = Button(frame1, image=OneHour_btn, borderwidth=0, bg="#707c74", highlightthickness=0, bd=0).grid(row=5, column=3, padx=10, pady=10)
PomodoroButton = Button(frame1, image=Pomodoro_btn, borderwidth=0, bg="#707c74", highlightthickness=0, bd=0).grid(row=5, column=4, padx=10, pady=10)
CustomButton = Button(frame1, image=Custom_btn, borderwidth=0, bg="#707c74", highlightthickness=0, bd=0).grid(row=5, column=5, padx=10, pady=10)

ExitButton = Button(frame1, image=Exit_btn, borderwidth=0, command=exit, bg="#707c74", highlightthickness=0, bd=0).grid(row=7, column=3, padx=10, pady=10, columnspan=2)

# Adding navigate to statistics tab button:
# navigateButton = Button(frame1, text = "To tab 2", command = select).grid(row = 1, column = 1, padx=10, pady=10)

# Adding exit button:
# exitButton = Button(frame1, width = 18, height = 3, padx=10, pady=10, text = "Exit", font = buttonFont1, command = root.quit).grid(row = 3, column = 4)


# End "loop" of interface:
root.mainloop()
