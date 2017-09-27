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

    def count_letters(self, word):
        letter_number = {}
        for letter in word:
            if letter in letter_number:
                letter_number[letter] += 1
            else:
                letter_number[letter] = 1
        return letter_number

class Fibonacci(object):

    def fibonacci(self, n):
        if n < 2:
            return n
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)