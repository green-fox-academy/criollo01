# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

import statistics

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5]

def odd_average(list):
    odd_list = []
    for i in list:
        if i % 2 != 0:
            odd_list.append(i)
    return statistics.mean(odd_list)

print(odd_average(list))