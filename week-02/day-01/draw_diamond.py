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

for i in range(0, number):
    print(" " * (number - i) + "*" * (i * 2 - 1))