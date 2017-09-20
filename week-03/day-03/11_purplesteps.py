from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

x = 0
y = 0

def purple_steps(x, y):
    square = canvas.create_rectangle(x, y, x + 10, y + 10, fill="purple")

for i in range(1, 20):
    x += 10
    y += 10
    purple_steps(x, y)

root.mainloop()