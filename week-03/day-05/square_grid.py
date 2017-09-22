from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'black')
canvas.pack()

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

def rectangle(x, y, width):
    canvas.create_rectangle(x - width/2, y - width/2, x + width/2, y + width/2, outline = random.choice(colors))

def many_rectangles(x, y, size):
    if size < 5:
        return
    new_size = size / 2
    rectangle(x, y, size)
    many_rectangles(x - new_size, y - new_size, new_size)
    many_rectangles(x + new_size, y - new_size, new_size)
    many_rectangles(x - new_size, y + new_size, new_size)
    many_rectangles(x + new_size, y + new_size, new_size)





many_rectangles(150, 150, 150)

root.mainloop()