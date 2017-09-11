# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

number = int(raw_input("Write a number and Imma tell you if it's even or odd: "))
if number % 2 == 0:
    print("It's even!")
else:
    print("It's odd!")