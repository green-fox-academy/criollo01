# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def go_to_center(x, y):
    line = canvas.create_line(x, y, 150, 150, fill = 'red')

go_to_center(10, 25)
go_to_center(200, 40)
go_to_center(3, 250)

root.mainloop()