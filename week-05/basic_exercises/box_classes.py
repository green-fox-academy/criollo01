# Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume

class Cuboid():
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_surface(self):
        return 2 * (self.side_a * self.side_b) + (self.side_b * self.side_c) + (self.side_a * self.side_c)

    def get_volume(self):
        return self.side_a * self.side_b * self.side_c

box = Cuboid(2, 5, 3)
print(box.get_surface())
print(box.get_volume())
