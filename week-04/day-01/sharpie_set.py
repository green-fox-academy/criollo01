from sharpie import Sharpie

class SharpieSet(object):
    def __init__(self):
        self.sharpies = [Sharpie("yellow", 10.5), Sharpie("green", 20), Sharpie("black", 5), Sharpie("blue", 12)]

    def count_usable(self):
        self.usable_sharpies = 0
        for sharpie in self.sharpies:
            if sharpie.ink_amount > 0:
                self.usable_sharpies += 1
        return self.usable_sharpies
    
    def remove_trash(self):
        for sharpie in self.sharpies:
            if sharpie.ink_amount <= 0:
                self.sharpies.remove(sharpie)
        return self.sharpies

sharpie_set = SharpieSet()

sharpie_set.sharpies[1].use(100)
sharpie_set.sharpies[0].use(100)

print(sharpie_set.count_usable())
print(sharpie_set.remove_trash())