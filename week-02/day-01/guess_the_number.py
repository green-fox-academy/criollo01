# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

print("I will think of a number and you can guess it.")
print("I thought of a number.")
number = 6
guess_number = int(input("Write your guess! "))

while guess_number != number:
    print("Guess again!")
    if guess_number > number:
        print("The stored number is lower")
        guess_number = int(input("Write your guess! "))
    else:
        print("The stored number is higher")
        guess_number = int(input("Write your guess! "))
if guess_number == number:
    print("You found the number: " + str(number))
