# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def horizontal_lines(x, y):
    line = canvas.create_line(x, y, x+50, y, fill = 'blue')

horizontal_lines(20, 20)
horizontal_lines(60, 200)
horizontal_lines(1, 280)

root.mainloop()