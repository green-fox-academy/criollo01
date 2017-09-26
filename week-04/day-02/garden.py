class Garden(object):

    def __init__(self):
        self.plants = []

    def add(self, plant):
        self.plants.append(plant)

    def water(self, amount):
        print("Watering with {} amount".format(amount))
        self.watering = []
        for plant in self.plants:
            if plant.needs_water() == "needs water":
                self.watering.append(plant)
        for plant in self.watering:
            plant.watered(amount/len(self.watering))
        return(self)

    def __repr__(self):
        all_plants = ""
        for i in range(len(self.plants)):
             all_plants += str(self.plants[i]) + "\n"
        return all_plants

class Plants(object):

    def __init__(self, color):
        self.color = color
        self.water_amount = 0

class Tree(Plants):

    def needs_water(self):
        if self.water_amount < 10:
            return "needs water"
        else:
            return "doesn't need water"

    def watered(self, amount):
        self.water_amount += amount * 0.4
    
    def __repr__(self):
        return "The {} tree {}.".format(self.color, self.needs_water())

class Flower(Plants):

    def needs_water(self):
        if self.water_amount < 5:
            return "needs water"
        else:
            return "doesn't need water"

    def watered(self, amount):
        self.water_amount += amount * 0.75

    def __repr__(self):
        return "The {} flower {}.".format(self.color, self.needs_water())

the_garden = Garden()
the_garden.add(Tree("brown"))
the_garden.add(Tree("green"))
the_garden.add(Flower("red"))
the_garden.add(Flower("yellow"))

print(the_garden)

the_garden.water(40)

print(the_garden)

the_garden.water(70)

print(the_garden)