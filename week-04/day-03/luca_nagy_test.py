import unittest
from luca_nagy_work import Apple, Sum, Anagram

class AppleTestCases(unittest.TestCase):

    def test_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), "apple")

class SumTestCases(unittest.TestCase):

    def test_sum(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([1, 2, 3]), 6)

    def test_sum_if_empty(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([]), 0)

    def test_if_one_element(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([1]), 1)

    def test_if_multiple_element(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum([1, 2, 3, 4, 5]), 15)

    def test_if_null(self):
        test_list_of_numbers = Sum()
        self.assertEquals(test_list_of_numbers.sum(None), None)       

class AnagramTestCase(unittest.TestCase):

    def test_anagram(self):
        test_anagram = Anagram()
        self.assertTrue(test_anagram)

class CountLettersTestCase(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(letter_counter(""), {})
        
    def test_one_letter(self):
        self.assertEqual(letter_counter("a"), {"a": 1})
        self.assertEqual(letter_counter("b"), {"b": 1})

    def test_two_different_letters(self):
        self.assertEqual(letter_counter("ab"), {"a": 1, "b": 1})

    def test_two_same_letters(self):
        self.assertEqual(letter_counter("aa"), {"a": 2})




if __name__ == '__main__':
    unittest.main()