# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

step = 20

def line_drawing_to_center(x, y):
    canvas.create_line(x, y, 150, 150, fill = 'green')

for n in range(16):
    line_drawing_to_center(n * step, 0)
    line_drawing_to_center(0, n * step)
    line_drawing_to_center(n * step, 300)
    line_drawing_to_center(300, n * step)




root.mainloop()