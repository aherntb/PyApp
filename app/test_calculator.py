"""Tests for the calculator module"""

import unittest
from science import calculator


class CalculatorTests(unittest.TestCase):
    """Test Class for the Calculator module

    Args:
        unittest (_type_): Unit test
    """

    def test_add_numbers_five_plus_five_equals_ten(self):
        """Add numbers should sum 5 & 5 and return 10 """
        num_one = 5
        num_two = 5
        result = calculator.add_numbers(num_one, num_two)

        self.assertEqual(result, 10, 'Result was not correctly calculated')

    def test_add_numbers_when_invoked_with_strings_throws_exception(self):
        """Add numbers should throw exception when invoked with strings"""
        num_one = 'string instead of number'
        num_two = 'another string instead of number'

        self.assertRaises(TypeError, calculator.add_numbers, num_one,
                          num_two, "Exception should be thrown for strings")

    def test_subtract_from_num_seven_from_ten_is_three(self):
        """Subtract from num should return 3 when 7 is taken from 10 """
        num_one = 10
        num_two = 7
        result = calculator.subtract_from_num(num_one, num_two)

        self.assertEqual(result, 3, 'Result was not correctly calculated')

    def test_subtract_from_num_when_invoked_with_strings_throws_exception(self):
        """Subtract from num should throw exception when invoked with strings"""
        num_one = 'string instead of number'
        num_two = 'another string instead of number'

        self.assertRaises(TypeError, calculator.subtract_from_num, num_one,
                          num_two, "Exception should be thrown for strings")


if __name__ == '__main__':
    unittest.main()
