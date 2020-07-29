'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
import unittest

from my_average import average


class TestAverage(unittest.TestCase):
    def test_list_int(self):
        """test: average a list of integers"""
        data = [1, 2, 3]
        result = average(data)
        self.assertEqual(result, 2)

    def test_list_fraction(self):
        """test: average a list of fractions"""
        data = [1/4, 1/3, 2/3]
        result = average(data)
        self.assertEqual(result, 1.25)

    def test_zero_division(self):
        data = []
        with self.assertRaises(ZeroDivisionError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()