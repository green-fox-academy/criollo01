import unittest
from luca_nagy_work import Apple, Sum, Anagram, CountLetters, Fibonacci

class AppleTestCases(unittest.TestCase):

    def test_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), "apple")

class SumTestCases(unittest.TestCase):

    def test_sum(self):
        test_list_of_numbers = Sum()
        self.assertEqual(test_list_of_numbers.sum([1, 2, 3]), 6)

    def test_sum_if_empty(self):
        test_list_of_numbers = Sum()
        self.assertEqual(test_list_of_numbers.sum([]), 0)

    def test_if_one_element(self):
        test_list_of_numbers = Sum()
        self.assertEqual(test_list_of_numbers.sum([1]), 1)

    def test_if_multiple_element(self):
        test_list_of_numbers = Sum()
        self.assertEqual(test_list_of_numbers.sum([1, 2, 3, 4, 5]), 15)

    def test_if_null(self):
        test_list_of_numbers = Sum()
        self.assertEqual(test_list_of_numbers.sum(None), None)       

class AnagramTestCase(unittest.TestCase):

    def test_anagram(self):
        test_anagram = Anagram()
        self.assertTrue(test_anagram)


class CountLettersTestCase(unittest.TestCase):

    def test_if_empty(self):
        test_word = CountLetters()
        self.assertEqual(test_word.count_letters(""), {})
    
    def test_if_one(self):
        test_word = CountLetters()
        self.assertEqual(test_word.count_letters("kutya")["k"] , 1)

    def test_if_two_same(self):
        test_word = CountLetters()
        self.assertEqual(test_word.count_letters("hamar")["a"] , 2)


class FibonacciTestCases(unittest.TestCase):

    def test_if_less_than_two(self):
        test_number = Fibonacci()
        self.assertTrue(test_number.fibonacci(1), 1)

    def test_if_two(self):
        test_number = Fibonacci()
        self.assertTrue(test_number.fibonacci(2), 2)      

    def test_if_bigger_than_two(self):
        test_number = Fibonacci()
        self.assertTrue(test_number.fibonacci(3), 55)

if __name__ == '__main__':
    unittest.main()