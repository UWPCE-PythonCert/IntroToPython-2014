#!/usr/bin/env python

"""
quadratic function evaluator:

example of callable functions
"""


class Quadratic(object):
    """
    class for evaluating the quadratic equation
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return (self.a * x**2) + (self.b * x) + self.c


