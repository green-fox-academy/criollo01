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
        print(self)

