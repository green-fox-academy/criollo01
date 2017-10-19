# def median(pool):
#     return pool[int((len(pool) - 1) / 2)]

def median(pool):
    pool.sort()
    if len(pool) < 1:
        return None
    if len(pool) % 2 == 0:
        return (pool[(len(pool) / 2)] + pool[(len(pool) / 2) -1]) / 2
    else:
        return pool[len(pool) / 2]


# test:

import unittest
import median

class TestMedian(unittest.TestCase):
    def setUp(self):
        pass

    def test_median_four(self):
        self.assertEqual(median.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(median.median([1,2,3,4,5]), 3)
        
if __name__ == '__main__':
    unittest.main()


# how can I make it simpler to read?

def median(pool):
    pool.sort()
    half = len(pool) // 2   #--> take a half variable in
    if len(pool) < 1:
        return None
    if len(pool) % 2 == 0:
        return (pool[half] + pool[half -1]) / 2
    else:
        return pool[half]

# another, simpler solution:


from statistics import median

pool = [1, 2, 3, 6, 8]

median(pool)