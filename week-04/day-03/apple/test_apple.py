import unittest
from apple import Apple

class TestApple(unittest.TestCase):
    
    def test_get_apple(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), "peach")

if __name__ == '__main__':
    unittest.main()