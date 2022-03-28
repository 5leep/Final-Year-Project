import tkinter as tk

Height = 720
Width = 1280

root = tk.Tk()

canvas = tk.Canvas(root, height = Height, width = Width)
canvas.pack()

button = tk.Button(root, text="Test button", fg='white', bg='black')
button.pack()

root.mainloop()
