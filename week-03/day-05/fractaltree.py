from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'black')
canvas.pack()

def draw_line(x1, y1, x2, y2, size):
    canvas.create_line(x1, y1, x2, y2, fill = 'white')

size = 160

def tree_drawing(x1, y1, size):
    if size < 5:
        return
    size = size / 2
    draw_line(x1, y1, x1, y1 - size, size)
    tree_drawing(x1, y1, size)


tree_drawing(150, 295,  size)
tree_drawing(x1 / 1.6, y1 / 1.6, size / 1.6)

root.mainloop()