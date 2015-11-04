#!/usr/bin/env python

"""
pytest example of a parameterized test

NOTE: there is a failure in here! can you fix it?

"""
import pytest

<<<<<<< HEAD
=======

>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f
# a (really simple) function to test
def add(a, b):
    """
    returns the sum of a and b
    """
    return a + b

# now some test data:

<<<<<<< HEAD
test_data = [ ( ( 2,  3),  5),
              ( (-3, 2), -1),
              ( ( 2, 0.5), 2.5),
              ( ( "this", "that"), "this that"),
              ( ( [1,2,3], [6,7,8]), [1,2,3,6,7,8]),
              ]
=======
test_data = [((2, 3), 5),
             ((-3, 2), -1),
             ((2, 0.5), 2.5),
             (("this", "that"), "this that"),
             (([1, 2, 3], [6, 7, 8]), [1, 2, 3, 6, 7, 8]),
             ]

>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f

@pytest.mark.parametrize(("input", "result"), test_data)
def test_add(input, result):
    assert add(*input) == result
<<<<<<< HEAD

=======
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f
