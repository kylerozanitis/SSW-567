""" 
This program contains three functions: classify_triange(), bad_classify_triangle()
and valid_input(). 

The classify_triangle() function takes three inputs, the three sides
of a triangle, and returns "Equilateral" if all three sides are equal, "Isoceles"
if two sides are equal, "Scalene" if none of the sides are equal, "Not A Triangle"
if the sum of two of the sides is less than the length of the third side, and
"Right" if the sum of the square of two of the sides equals the square of the 
remaining side.  

The bad_classify_triangle() function attempts to do what the classify_triangle()
function does, but has some bugs in it to illustrate that the test cases work.

The valid_input function() verifies that the inputs can be converted into floats
and that the values are greater than 0 and less than 100.
"""


def valid_input(number):
    """ This function takes any input and tries to convert it into a float. If
    the value cannot be converted into a float, then an error statement is
    printed and False is returned. If the number can be converted into a float,
    the converted input is checked to ensure it is greater than 0 and less
    than 100. The specification did not specify a max size for a side of a
    triangle, so I assumed 100. """

    try:
        converted_input = float(number)
    except ValueError:
        print("You have entered an invalid value. Please enter an integer " \
              "or float greater than 0 and less than 100.")
        return False

    if converted_input > 0 and converted_input < 100:
        return converted_input
    else:
        return False


def bad_classify_triangle(side1, side2, side3):
    """ This function is to illustrate that the test cases work. It does not
    validate the input and omits key logic about triangles (i.e. does not
    include logic for checking for right triangle). """

    if side1 == side2 and side1 == side3 and side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Scalene"
    elif (side1 != side2 and side1 != side3) or (side1 == side3 and side1 != side2) or (side2 == side3 and side2 != side1):
        return "Isoceles"
    else:
        "Not A Triangle"