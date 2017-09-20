# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def center_box(size):
    square = canvas.create_rectangle(150-size/2, 150-size/2, 150+size/2, 150+size/2, outline = 'black')

center_box(30)
center_box(70)
center_box(130)

root.mainloop()