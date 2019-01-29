"""
This file contains the tests for HW 01: Testing Triangle Classification

By Kyle Rozanitis
SSW-567
"""

# Library Imports
import unittest

# File Imports
import classify_triangle as ct

class TestValidInput(unittest.TestCase):
    """ Unit tests to verify that the functions in classify_triangle.py 
    work as expected. """

    def test_valid_input(self):
        """ Unit tests to verify that the valid_input function works
        as expected. """

        self.assertEqual(ct.valid_input(3), 3.0)
        self.assertEqual(ct.valid_input(4.5), 4.5)
        self.assertEqual(ct.valid_input("5"), 5.0)
        self.assertEqual(ct.valid_input("Number"), False)
        
    def test_bad_classify_triangle(self):
        """ Unit tests to verify that the bad_classify_triangle function
        works as expected. """

        self.assertEqual(ct.bad_classify_triangle(3,3,3), "Equilateral")
        self.assertEqual(ct.bad_classify_triangle(3,4,5), "Isoceles")
        self.assertNotEqual(ct.bad_classify_triangle(7,24,25), "Right")
        self.assertEqual(ct.bad_classify_triangle(3,3,5), "Scalene")
        self.assertNotEqual(ct.bad_classify_triangle(3,4,"huh"), "Not A Triangle")
    
    def test_classify_triangle(self):
        """ Unit tests to verify that the classify_triangle function works
        as expected and fixes the errors with the bad_classify_triangle funciton. """

        self.assertEqual(ct.classify_triangle(3.0, 3, 3.0001), "Equilateral")
        self.assertEqual(ct.classify_triangle(3.0, 3, 5), "Scalene")
        self.assertEqual(ct.classify_triangle(7.0, 24.003, 25), "Right")
        self.assertEqual(ct.classify_triangle(4, 6, 9), "Isoceles")
        self.assertEqual(ct.classify_triangle(4, 6, "huh"), "One of your inputs in invalid. Please enter three integers or floats.")


if __name__ == '__main__':
    unittest.main(exit=False,verbosity=2)