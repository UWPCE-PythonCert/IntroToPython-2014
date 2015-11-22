__author__ = 'ryan.morin'

import math

def sine(x):
    return math.sin(x)

def line(x):
    return 5

def quadratic(x, c=0, d=0, e=0):
    return c * x**2 + d*x + e

def trapz(fun, a, b, *args, **kwargs):
    """
    Compute the area under the curve from 'a' to 'b' for a function y = f(x)
    :param fun: the function used for the calculation
    :param a: the beginning point of the integration
    :param b: the ending point of the integration
    :return: the area of the function fun
    """
    total = 0.0
    inc = float((b-a))/100
    total += fun(a)/2.0
    for i in range(1,100):
        total += fun(a + (i * inc))
    total += (fun(b)/2.0)
    return total * inc

print (trapz(lambda x: math.sin(x), 1,10))