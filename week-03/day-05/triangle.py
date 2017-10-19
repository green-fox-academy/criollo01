from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'black')
canvas.pack()

colors = ["red", "orange", "yellow", "green", "blue", "violet"]

def triangle(x, y,width):
    canvas.create_polygon(x - width/2, y - width/2, x + width/2, y - width/2, x, y + width/2, outline = random.choice(colors))

def many_triangles(x, y, size):
    if size < 140:
        return
    new_size = size / 2
    triangle(x, y, size*2)
    many_triangles(x - new_size, y - new_size, size)
    many_triangles(x + new_size, y - new_size, size)
    many_triangles(x, y + new_size, size)






many_triangles(150, 150, 150)

root.mainloop()