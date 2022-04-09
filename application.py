# Imports:
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter.ttk import Style


# Begin "loop" of interface:

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
notebook.pack(pady = 15)

# Go to Statistics tab function:
def select():
    notebook.select(1)


# Creating tabs:
frame1 = Frame(notebook, width=screenWidth, height=screenHeight, bg="#6e7a74")
frame2 = Frame(notebook, width=screenWidth, height=screenHeight, bg="white")

# Packing tabs:
frame1.pack(fill = "both", expand = 1)
frame2.pack(fill = "both", expand = 1)

# Adding tabs, allowing functionality and title:
notebook.add(frame1, text = "Timer")
notebook.add(frame2, text = "Statistics")


# Setting up fonts:
# buttonFont1 = font.Font(family = 'Helvetica', size = 12, weight= 'bold')
buttonFont2 = font.Font(family = 'Helvetica', size = 10)
timerFont1 = font.Font(family = 'Calibri', size = 40, weight = 'bold')


# Adding Labels:
# Timer Label:
timer = Label(frame1, text = "00:00", font = timerFont1).grid(row = 3, column = 3, columnspan = 1, rowspan = 1, padx=10, pady=40)
blankLabel1 = Label(frame1, text = "        ", font = timerFont1, fg = "#6e7a74", bg = "#6e7a74").grid(row = 1, column = 1)
blankLabel2 = Label(frame1, text = "        ", font = timerFont1, fg = "#6e7a74", bg = "#6e7a74").grid(row = 2, column = 1)

# Setting images for buttons:
Start_btn = PhotoImage(file = 'media/Start_btn.png')
Start_btn.zoom(200, 200)
Stop_btn = PhotoImage(file = 'media/Stop_btn.png')
pomodoro_btn = PhotoImage(file = 'media/pomodoro_btn.png')
custom_btn = PhotoImage(file = 'media/custom_btn.png')

# Adding start and stop buttons
startButton = Button(frame1, image = Start_btn, borderwidth = 0).grid(row = 3, column = 2, padx=10, pady=10)
stopButton = Button(frame1, text = "STOP", width = 18, height = 3).grid(row = 3, column = 4, padx=10, pady=10)

# Adding navigate to statistics tab button:
# navigateButton = Button(frame1, text = "To tab 2", command = select).grid(row = 1, column = 1, padx=10, pady=10)

# Adding exit button:
# exitButton = Button(frame1, width = 18, height = 3, padx=10, pady=10, text = "Exit", font = buttonFont1, command = root.quit).grid(row = 3, column = 4)


# End "loop" of interface:
root.mainloop()
