__author__ = 'ryan.morin'

def line(x):
    return 5

def quadratic(x, c=0, d=0, e=0):
    return c * x**2 + d*x + e

def frange(a,b,n):
    delta = float((b-a))/n
    return [a + i * delta for i in range(n+1)]

def trapz(fun, a, b, *args, **kwargs):
    """
    Compute the area under the curve from 'a' to 'b' for a function y = f(x)
    :param fun: the function used for the calculation
    :param a: the beginning point of the integration
    :param b: the ending point of the integration
    :return: the area of the function fun
    """
    total = 0.0
    n = 100
    vals = frange(a,b,n)
    inc = float(b-a)/n
    total += (fun(a, *args, **kwargs) + fun(b, *args, **kwargs))/2.0
    total = sum([fun(x, *args, **kwargs) for x in vals[1:-1]])
    return total