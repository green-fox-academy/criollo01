from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def purple_steps():
    x = 0
    y = 0
    size = 10
    for i in range(1, 8):
        x_extended = x + size
        y_extended = y + size
        square = canvas.create_rectangle(x, y, x + size, y + size, fill="purple")
        size += 10
        x = x_extended
        y = y_extended
purple_steps()

root.mainloop()