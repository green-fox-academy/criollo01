class Apple(object):

    def get_apple(self):
        return "apple"


class Sum(object):

    def sum(self, list_of_numbers):
        if list_of_numbers == None:
            return None
        else:
            return sum(list_of_numbers)


class Anagram(object):

    def anagram(self, list1, list2):
        compare = list(list1)
        compare_to = list(list2)
        if compare.sort() == compare_to.sort():
            return True 

class CountLetters(object):
    
    def count_letters(self):
          output = {}
        for letter in word:
            if letter in output:
                output[letter] += 1
            else:
                output[letter] = 1
        return output

class Fibonacci(object):
    
    def fibonacci(number):
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        else:
            return fibonacci(number - 1) + fibonacci(number - 2)