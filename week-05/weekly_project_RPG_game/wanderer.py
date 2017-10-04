from tkinter import *
from map_drawer import MapTiles

root = Tk()
canvas = Canvas(root, width = 720, height = 720, bg="white", bd=0)

map_drawer = MapTiles()

class Tile():

    def __init__(self):
        self.floor = PhotoImage(file = 'assets/floor.png')
        self.wall = PhotoImage(file = 'assets/wall.png')
        self.draw_map(map_drawer.tiles)

    def draw_map(self):
        for y in range(len(map_drawer.tiles)):
            for x in range(len(map_drawer.tiles)):
                if map_drawer.tiles[y][x] == 0:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.floor)
                else:
                    canvas.create_image(x*72, y*72, anchor = NW, image = self.wall)


class Entity():

    def __init__(self):
        self.image_boss = PhotoImage(file = 'assets/boss.png')
        self.image_skeleton = PhotoImage(file = 'assets/skeleton.png')
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)
        self.id = 0

    def draw_skeleton(self, canvas):
        canvas.delete(self.id)
        self.id = canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = self.image_skeleton)

    def draw_boss(self, canvas):
        canvas.delete(self.id)
        self.id = canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = self.image_boss)


class Hero():

    def __init__(self):
        self.hero = PhotoImage(file = 'assets/hero-down.png')
        self.hero_right = PhotoImage(file = 'assets/hero-right.png')
        self.hero_left = PhotoImage(file = 'assets/hero-left.png')
        self.hero_up = PhotoImage(file = 'assets/hero-up.png')
        self.x = 0
        self.y = 0
        self.id = 0

    def draw_hero(self, canvas, hero_image):
        canvas.delete(self.id)
        self.id = canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = hero_image)


class View():
    pass

class GameLogic():
    def __init__(self):
        root.bind("<KeyPress>", self.on_key_press)
        self.floor = Tile()
        self.hero = Hero()
        self.floor.draw_map()
        self.hero.draw_hero(canvas, self.hero.hero_down)

    def is_it_free_for_hero(self, x, y):
        if 0 <= x <= 9 and 0 <= y <= 9:
            if self.floor.tiles[y][x] == 0:
                self.hero.draw_hero(canvas, self.hero.hero_down)
                self.hero.x = x
                self.hero.y = y

    def on_key_press(self, e):
        self.e = e 
        
        if self.e.keycode == 37:
            self.move_hero(self.hero.x - 1, self.hero.y)
            self.hero.draw_hero(canvas, self.hero.hero_left)
        elif self.e.keycode == 38:
            self.move_hero(self.hero.x, self.hero.y - 1)
            self.hero.draw_hero(canvas, self.hero.hero_up)
        elif self.e.keycode == 39:
            self.move_hero(self.hero.x + 1, self.hero.y)
            self.hero.draw_hero(canvas, self.hero.hero_right)
        elif self.e.keycode == 40:
            self.move_hero(self.hero.x, self.hero.y + 1)
            self.hero.draw_hero(canvas, self.hero.image_hero_down)

game = GameLogic()
canvas.pack()
canvas.focus_set()
root.mainloop()