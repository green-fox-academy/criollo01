from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'green')
canvas.pack()

def rectangle(x, y, width):
    canvas.create_rectangle(x, y, x + width, y + width, outline = 'black')

def many_rectangles(x, y, size):
    if size < 10:
        return
    size = size / 3
    rectangle(x + size, y, size)
    rectangle(x, y + size, size)
    rectangle(x + size, y + (2 * size), size)
    rectangle(x + (2 * size), y + size, size)

    many_rectangles(x + size, y, size)
    many_rectangles(x, y + size, size)
    many_rectangles(x + size, y + (2 * size), size)
    many_rectangles(x + (2 * size), y + size, size)
    
many_rectangles(0, 0, 300)

root.mainloop()