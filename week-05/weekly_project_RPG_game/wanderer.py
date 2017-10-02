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


class Hero():

    def __init__(self):
        self.hero = PhotoImage(file = 'assets/hero-down.png')
        self.draw_hero()

    def draw_hero(self):
        self.entity_img = canvas.create_image(0, 0, anchor = NW, image = self.hero)
    
class Entity():
    def __init__(self):
        pass

    def move(self, dx, dy):
        canvas.move(entity.entity_img, dx, dy )

entities = Entity()

def moving(e):
    if (e.keysym == 'Up'):
        entities.move(0,-72)
    elif (e.keysym == 'Down'):
        entities.move(0,72)
    elif (e.keysym == 'Right'):
        entities.move(72,0)            
    elif (e.keysym == 'Left'):
        entities.move(-72,0)

class View():
    pass

class GameLogic():
    pass

canvas.pack()

map_draw = Tile()
entity = Hero()
root.bind("<KeyPress>", moving)
canvas.focus_set()
root.mainloop()