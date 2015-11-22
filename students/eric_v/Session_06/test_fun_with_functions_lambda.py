"""
some simple tests for the fun_with_functions.py

designed to run with py.test or nose.
"""

#from fun_with_functions_lambda import evaluate_function

#def test_evaluate_function():
#    """
#    the function should evaluate the expression
#    """
#    assert evaluate_function(0) == 3

#    assert evaluate_function(3) == 12

#    assert evaluate_function(5) == 28



from fun_with_functions_lambda import increment_size

def test_increment_size():
    """
    this function determines the size of each increment
    """
    assert increment_size(1, 2, 5) == 0.20

    assert increment_size(0, 2, 8) == 0.25

    assert increment_size(4, 7, 3) == 1.0



def evaluate_increment_lambda(lower_boundary, upper_boundary):
    lower_boundary_height = evaluate_function(lower_boundary)
    upper_boundary_height = evaluate_function(upper_boundary)
    print ('lower_value = ', lower_boundary_height)
    print ('upper_value = ', upper_boundary_height)
    increment_area = ((lower_boundary_height + upper_boundary_height)/2) * (upper_boundary - lower_boundary)
    return increment_area
from fun_with_functions import increment_size

#def test_trapz():
#    """
#    this function determines the area associated with each increment
#    """
#    assert trapz(1.0, 1.25) == 1.0703125

#    assert trapz(1.25, 1.50) == 1.2265625

#    assert trapz(1.50, 1.75) == 1.4140625
