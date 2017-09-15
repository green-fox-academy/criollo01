import random

number_of_guesses = 0
number = random.randint(1, 100)
lives = int(input('How many lives do you want for your game?'))

print('I thought of a number between 1 and 100')
while number_of_guesses < lives:
    print('Try to guess the number!:')
    guess = int(input())
    number_of_guesses = number_of_guesses + 1
    remaining = str(lives - number_of_guesses)

    if guess < number:
        print('Too low. You have ' + remaining + ' lives left.')
    elif guess > number:
        print('Too high. You have ' + remaining + ' lives left.')
    elif guess == number:
        print("Congrats!")


if guess != number:
    number = str(number)
    print('Nope. The number was ' + number + ".")

if number_of_guesses == lives:
    print('Your lives are lost. You can try again another time.')