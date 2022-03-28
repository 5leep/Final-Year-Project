import tkinter as tk

# Variables for size of window:
Height = 720
Width = 1280

# Begin "loop" of interface:
root = tk.Tk()

# Create and pack canvas (window):
canvas = tk.Canvas(root, height = Height, width = Width)
canvas.pack()

# Create and place frame (on top of, and relative to, canvas):
frame = tk.Frame(root, bg='blue')
frame.place(relwidth=0.8, relheight=0.8)

# Create and pack button:
button = tk.Button(root, text="Test button", fg='white', bg='black')
button.pack()

# End "loop" of interface:
root.mainloop()
