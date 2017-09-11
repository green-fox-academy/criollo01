# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

a = int(raw_input("Write a number! "))
b = int(raw_input("Write one more! "))
c = int(raw_input("And one more! "))
d = int(raw_input("And one more! "))
e = int(raw_input("And one more! "))

print("Sum:", (a+b+c+d+e), ", Average:", ((a+b+c+d+e) / 5))