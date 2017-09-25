class Sharpie(object):
    def __init__(self, color, width):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = 100

    def use(self, amount):
        self.ink_amount -= amount
        return self.ink_amount

yellow = Sharpie("yellow", "1.2")
black = Sharpie("black", "2.3")
blue = Sharpie("blue", "4")

yellow.use(50)
print(yellow.ink_amount)
blue.use(20)
blue.use(2)
print(blue.ink_amount)