
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

# Create and pack canvas (window):
canvas = tk.Canvas()
canvas.pack()

# Create and place frame (on top of, and relative to, canvas):
frame = tk.Frame(root, bg='#77af87')
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

# Create and pack START button:
button = tk.Button(frame, text="Start", fg='white', bg='black')
button.place(x=100, y=100)
# Create and pack STOP button:
button = tk.Button(frame, text="Stop", fg='white', bg='black')
button.place(x=150, y=150)

# Create and pack label:
label = tk.Label(frame, text="This is a label", fg='black', bg='white')
label.pack()

# Create and pack entry:
entry = tk.Entry(frame, bg='green')
entry.pack()

# End "loop" of interface:
root.mainloop()
