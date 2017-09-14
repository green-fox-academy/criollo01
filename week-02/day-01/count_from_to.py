# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

number1 = int(input("Write a number! "))
number2 = int(input("Write another number!"))

if not number2 > number1:
    print("The second number should be bigger!")
else:
    for i in range(number1, number2 + 1):
        print(i)