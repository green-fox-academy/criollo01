import unittest
from fun import fun

class TestFun(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()