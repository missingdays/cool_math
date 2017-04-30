import sys

sys.path.insert(0, '../')
sys.path.insert(0, '../../')

import unittest
from cool_math import square

class TestSquare(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_positive(self):
        self.assertEqual(square(1), 1)
        self.assertEqual(square(3), 9)


    def test_negative(self):
        self.assertEqual(square(-1), 1)
        self.assertEqual(square(-3), 9)

if __name__ == "__main__":
    unittest.main()
