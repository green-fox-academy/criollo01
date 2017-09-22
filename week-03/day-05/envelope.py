from tkinter import *
import random

root = Tk()



canvas = Canvas(root, width='700', height='700', bg = 'black')
canvas.pack()

color = ['blue', 'green', 'red', 'yellow', 'brown', 'purple', 'white', 'orange']

def envelope(x, y, a, b):
    line = canvas.create_line(x, y, a, b, fill = random.choice(color))

i = 0
while i < 350:
    i += 10
    envelope(350, i, 350-i, 350)
    envelope(350, i, 350+i, 350)
    envelope(350-i, 350, 350, 700-i)
    envelope(350+i, 350, 350, 700-i)

root.mainloop()
