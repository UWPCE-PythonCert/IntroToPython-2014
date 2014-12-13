#!/usr/bin/python

class Quadratic(object):

    def __init__(self, a, b,c):

        self.a = a
        self.b = b
        self.c = c

    def __call__(self,x):
        self.x = x

        return self.a * self.x**2 + self.b * self.x + self.c

my_quad = Quadratic(a=2, b=3, c=1)

my_quad(0)
