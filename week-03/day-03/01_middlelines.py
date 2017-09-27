# draw a red horizontal line to the canvas' middle.
# draw a green vertical line to the canvas' middle.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

red_rectangle = canvas.create_rectangle(0, 150, 300, 150, fill = 'red')


root.mainloop()