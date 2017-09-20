from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x = 0
y = 50
size = 50

for x in range(int(300/size)):
    for y in range(int(300/size)):
        color = "black" if (x+y) % 2 == 0 else "white"
        canvas.create_rectangle(size * x, size * y, size * (x + 1) , size * (y + 1), fill = color)

root.mainloop()