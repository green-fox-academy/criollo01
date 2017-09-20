from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def line_drawing(x, y, a, b, color):
    line = canvas.create_line(x, y, a, b, fill = color)

i = 0
while(i <= 300):
    line_drawing(0, i, i, 300, "green")
    i += 20

j = 0
while(j <= 300):
    line_drawing(300 - j, 0, 300, 300 - j, "purple")
    j += 20

root.mainloop()
