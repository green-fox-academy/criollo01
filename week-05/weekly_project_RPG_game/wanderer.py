from tkinter import *
from map_drawer import MapTiles

root = Tk()
canvas = Canvas(root, width = 720, height = 720, bg="white", bd=0)

map_drawer = MapTiles()

class Tile():

    def __init__(self):
        self.floor = PhotoImage(file = 'assets/floor.png')
        self.wall = PhotoImage(file = 'assets/wall.png')
        self.drawer(map_drawer.tiles)

    def drawer(self, map):
        for y in range(len(map_drawer.tiles)):
            for x in range(len(map_drawer.tiles)):
                if map_drawer.tiles[y][x] == 0:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.floor)
                else:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.wall)


class View():
    pass

class Entity():
    pass

class GameLogic():
    pass        

map_draw = Tile()

canvas.pack()
canvas.focus_set()
root.mainloop()