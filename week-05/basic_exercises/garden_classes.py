class Garden:

    def __init__(self):
        self.plants = []

    def add_plants(self, plant):
        self.plants.append(plant)

    def water(self, amount):
        print("Watering with {} amount of water".format(amount))
        self.watering = []
        for plant in self.plants:
            if plant.needs_water() == "needs water":
                self.watering.append(plant)
        for plant in self.watering:
            plant.watered(amount / len(self.watering))
        return(self)
    
    def __repr__(self):
        all_plants = ""
        for plant in range(len(self.plants)):
            all_plants += str(self.plants[plant]) + "\n"
        return all_plants


class Plants:

    def __init__(self, color):
        self.color = color
        self.water_amount = 0


class Flower(Plants):

    def needs_water(self):
        return "needs water" if self.water_amount < 5 else "doesn't need water"

    def watered(self, amount):
        self.water_amount += amount * 0.75
    
    def __repr__(self):
        return "The {} flower {}.".format(self.color, self.needs_water())


class Tree(Plants):

    def needs_water(self):
        return "needs water" if self.water_amount < 10 else "doesn't need water"

    def watered(self, amount):
        self.water_amount += amount * 0.4
    
    def __repr__(self):
        return "The {} tree {}.".format(self.color, self.needs_water())


class Grass(Plants):

    def needs_water(self):
         return "needs water" if self.water_amount < 50 else "doesn't need water"

    def watered(self, amount):
        self.water_amount += amount * 0.8

    def __repr__(self):
        return "The {} grass {}.".format(self.color, self.needs_water())


garden = Garden()
garden.add_plants(Flower("yellow"))
garden.add_plants(Flower("blue"))
garden.add_plants(Tree("brown"))
garden.add_plants(Tree("green"))
garden.add_plants(Grass("green"))

print(garden)

garden.water(40)

print(garden)

garden.water(70)

print(garden)

garden.water(90)

print(garden)