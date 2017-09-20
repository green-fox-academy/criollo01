# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

red_line = canvas.create_line(1, 1, 200, 1, fill = 'red')
blue_line = canvas.create_line(200, 1, 200, 200, fill = 'blue')
green_line = canvas.create_line(200, 200, 1, 200, fill = 'green')
purple_line = canvas.create_line(1, 200, 1, 1, fill = 'purple')

root.mainloop()