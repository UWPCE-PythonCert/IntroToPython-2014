#!usr/local/bin/python


class Quadratic(object):
    """
    Class for the quardratic equation.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        """
        Return the y value of the quadratic formula.
        """
        return (self.a * x ** 2) + (self.b * x) + self.c
