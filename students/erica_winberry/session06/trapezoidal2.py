'''
Update your trapz() function so that you can give it a function that
takes arbitrary extra arguments, either positional or keyword, after the x.
'''


def trapz(fun, start, stop, *args, **kwargs):
    # compute the area under an arbitrary function,
    # using the trapezoidal rule.

    values = x_values(start, stop)
    l = []

    # compute the function for each of those values and double them
    l.append(fun(values[0], *args, **kwargs))
    [l.append(2 * fun(value, *args, **kwargs)) for value in values[1:-1]]
    l.append(fun(values[-1], *args, **kwargs))

    # add the values all up
    total = sum(l)

    # multiply by the half of the difference between a and b div. by N.
    retval = ((stop-start)/2) * (total/len(values))
    return float(retval)


def x_values(a, b):
    # create a list of x values from a to b
    segment_count = 10000
    l = []
    l.append(a)
    [l.append(a+((i * (b-a))/segment_count))
        for i in range(1, segment_count)]
    l.append(b)
    return l


def line(y):
    return y


def quadratic(x, a=0, b=0, c=0):
    return (a * x**2) + (b * x) + c


def squared(x):
    return x * x

print(trapz(quadratic, 1, 10, a=1, b=3, c=2))
