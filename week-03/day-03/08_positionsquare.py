# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def position_square(x, y):
    square = canvas.create_rectangle(x, y, x+50, y+50, fill = 'green', anchor = tk.center)

position_square(200, 230)
position_square(30, 130)
position_square(70, 190)

root.mainloop()