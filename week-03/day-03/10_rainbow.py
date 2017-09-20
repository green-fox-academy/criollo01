# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def rainbow_square(size, color):
    left_top = 150 - (size / 2)  
    right_bottom = 150 + (size / 2)  
    square = canvas.create_rectangle(left_top, left_top, right_bottom, right_bottom, fill = color)

colors =["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(len(colors)):
    a = 300-i*25
    rainbow_square(a, colors[i])

root.mainloop()