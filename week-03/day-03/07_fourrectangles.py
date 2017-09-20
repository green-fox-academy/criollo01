# draw four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

rectangle_red = canvas.create_rectangle(0, 0, 55, 55, fill = 'red')
rectangle_blue = canvas.create_rectangle(40, 60, 130, 155, fill = 'blue')
rectangle_green = canvas.create_rectangle(140, 30, 155, 155, fill = 'green')
rectangle_yellow = canvas.create_rectangle(155, 170, 290, 280, fill = 'yellow')


root.mainloop()