# Imports:
import tkinter as tk
from tkinter import *
from tkinter import ttk

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
notebook.pack(pady=15)


# hide function:
def hide():
    notebook.hide(1)

# reveal function:
def show():
    notebook.add(frame2, text="Statistics")

def select():
    notebook.select(1)


# Creating tabs:
frame1 = Frame(notebook, width=screenWidth, height=screenHeight, bg="blue")
frame2 = Frame(notebook, width=screenWidth, height=screenHeight, bg="red")

# Packing tabs:
frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)

# Adding tabs, allowing functionality and title:
notebook.add(frame1, text="Timer")
notebook.add(frame2, text="Statistics")

# Adding hide and show buttons
startButton = Button(frame1, text="START", width=15, height=5, command=hide).grid(row=2, column=2)
stopButton = Button(frame1, text="STOP", width=15, height=5, command=show).grid(row=3, column=3)

# Adding navigate button:
navigateButton = Button(frame1, text="To tab 2", command=select).grid(row=1, column=1)

# End "loop" of interface:
root.mainloop()
