# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies 
# recursively (without loops or multiplication).

def bunnies_ears(bunny_number):
    if bunny_number <= 0:
        return 0
    else:
        return 2 + bunnies_ears(bunny_number - 1)

print(bunnies_ears(3))