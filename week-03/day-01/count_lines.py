# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

file_name = input("Add a filename! ")

def number_of_lines(file_name):
    try:
        opener = open(file_name, "r")
        count = sum(1 for line in open(file_name))
        print(count)
    except FileNotFoundError:
        return 0

number_of_lines(file_name)