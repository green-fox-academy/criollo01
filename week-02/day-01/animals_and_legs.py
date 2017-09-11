# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

chickens = int(raw_input("How many chickens does the farmer have? "))
pigs = int(raw_input("How many pigs does the farmer have? "))

print((chickens * 2) + (pigs * 4))