# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

number = int(input("Write a number! "))

# for i in range(0, number + 1):
#     print(" " * (number - i) + "*" * (i * 2 - 1))

if number > 0:
    for i in range(number):
        for s in range(number, -3, -2, -1):
            print(" ", end="")
        for j in range(i * 2 -1):
            print("*", end="")
        print()
    for i in range(number, -1, -1):
        for j in range(i * 2 -1):
            print("*", end="")
        print()