"""
This file contains the tests for HW 01: Testing Triangle Classification

By Kyle Rozanitis
SSW-567
"""

# Library Imports
import unittest

# File Imports
from classify_triangle import valid_input, bad_classify_triangle, classify_triangle

class TestValidInput(unittest.TestCase):
    """ Unit tests to verify that the functions in classify_triangle.py 
    work as expected. """

    def test_valid_input(self):
        """ Unit tests to verify that the valid_input function works
        as expected. """

        self.assertEqual(valid_input(3), 3.0)


if __name__ == '__main__':
    unittest.main(exit=False,verbosity=2)