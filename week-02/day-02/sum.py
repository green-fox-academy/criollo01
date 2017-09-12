# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum_list(numbers_list):
    sum = 0
    for i in numbers_list:
        sum += i
    return sum

numbers_list = [1, 2, 3, 4, 5]
print(sum_list(numbers_list))






#print(sum([1,2,3,4]))