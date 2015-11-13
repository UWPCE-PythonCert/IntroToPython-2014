'''
Your task is to write a trapz() function that will compute the area
under an arbitrary function, using the trapezoidal rule.

The function will take another function as an argument, as well as the
start and end points to compute, and return the area under the curve.
'''


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
    values = x_values(a, b)
    l = []
    l.append(fun(values[0]))
    [l.append(2 * fun(value)) for value in values[1:-1]]
    l.append(fun(values[-1]))
    total = sum(l)
    retval = ((b-a)/2) * (total/len(values))
    return float(retval)


def x_values(a, b):
    segment_count = 1000000
    l = []
    l.append(a)
    [l.append(a+((i * (b-a))/segment_count))
        for i in range(1, (segment_count+2))]
    l.append(b)
    return l


def line(y):
    return y


def squared(x):
    return x * x

print(trapz(line, 1, 10))

"""
result = b−a/2N(f(x1)+2f(x2)+2f(x3)+2f(x4)+...+2f(xN)+f(xN+1))

So you will need to:

-create a list of x values from a to b (maybe 100 or so values to start)


-compute the function for each of those values and double them


-add them all up

-multiply by the half of the difference between a and b.

Note that the first and last values are not doubled.

Can you use comprehensions for this?

NOTE: range() only works for integers – how can you deal with that?

Once you have that, it should work for any function that can be
evaluated between a and b.
"""