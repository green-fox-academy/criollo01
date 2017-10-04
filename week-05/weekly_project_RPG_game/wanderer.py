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


class Entity():
    def __init__(self):
        self.hero_down = PhotoImage(file = 'assets/hero-down.png')
        self.hero_up = PhotoImage(file = 'assets/hero-up.png')
        self.hero_right = PhotoImage(file = 'assets/hero-right.png')
        self.hero_left = PhotoImage(file = 'assets/hero-left.png')
        self.draw_hero()

    def move(self, dx, dy):
        canvas.move(hero.entity_img, dx, dy )

    def update_costume(self, costume):
        self.costume = costume
        canvas.itemconfigure(self.entity_img, image=self.costume)

    def draw_hero(self):
        self.entity_img = canvas.create_image(0, 0, anchor = NW, image = self.hero_down)

    def moving(self, e):
        if (e.keysym == 'Up'):
            self.move(0,-72)
            self.update_costume(self.hero_up)
        elif (e.keysym == 'Down'):
            self.move(0,72)
            self.update_costume(self.hero_down)
        elif (e.keysym == 'Right'):
            self.move(72,0)
            self.update_costume(self.hero_right)
        elif (e.keysym == 'Left'):
            self.move(-72,0)
            self.update_costume(self.hero_left)


class View():
    pass

class GameLogic():
    pass

canvas.pack()

map_draw = Tile()
hero = Entity()
root.bind("<KeyPress>", hero.moving)
canvas.focus_set()
root.mainloop()