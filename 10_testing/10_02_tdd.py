'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
import unittest

from my_calculator import *

class TestEverything(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(2, 3), 17)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(42, 7), 27)

    def test_divide(self):
        self.assertEqual(divide(1, 2), .5)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 4), 16)
