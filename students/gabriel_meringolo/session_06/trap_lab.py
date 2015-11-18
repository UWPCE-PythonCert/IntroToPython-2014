# create a list of x values from a to b (maybe 100 or so values to start)
# compute the function for each of those values and double them
# add them all up
# multiply by the half of the difference between a and b.
# Note that the first and last values are not doubled.



def trapz(fun, a, b):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    """
    n = 100
    delta_x = float(b - a) / n
    s = 0.0
    s += fun(a) / 2.0
    for i in range(1, n):
        s += fun(a + i * delta_x)
    s += fun(b) / 2.0 #
    return s * delta_x


f = lambda x: x**2

def line(x):
    '''a very simple straight horizontal line'''
    return 5

def quadratic(x, A=0, B=0, C=0):
    return A * x**2 + B * x + C

print(trapz(line, 0, 10))