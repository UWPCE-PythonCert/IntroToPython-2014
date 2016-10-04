#!/usr/bin/env python

"""
A simple set of examples that raise various Exceptions
"""


def name_error():
    """This function raises a NameError"""
    # very easy to do -- simply try to use a name you haven't defined
    x = something


def type_error():
    """This function raises a TypeError"""
    # Try to use an object in a way that doesn't make sense
    "543" / 3

def attribute_error():
    """This function raises an AttributeError"""
    x = 5
    y = x.strip()

# have to comment this out, because the SyntaxError keeps the code from
# running at all
# def syntax_error():
#     """This function raises a SyntaxError"""
#     del = 32  # this one is tricky -- it's an error because "del" is a keyword

# now run the functions:
# Note: I have all but one commented out, becaue the code stops running
#       when the first Error is hit.

# name_error()
# type_error()
attribute_error()
