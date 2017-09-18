# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0



def divide():
    number = int(input("Write a number! "))
    try:
        result = 10/number
        print(result)
    except ZeroDivisionError:
        print("Fail!")

divide()