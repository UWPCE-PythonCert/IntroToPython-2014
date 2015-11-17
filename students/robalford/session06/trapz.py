from math import sqrt
from functools import partial


def line(x):
    return 5


def a_curve(x):
    return sqrt(x-1)


def another_curve(x):
    return x**2 + 1

# quadratic with kwargs


def quadratic(x, A=0, B=0, C=0):
    return A * x**2 + B * x + C


def trapz(fun, a, b, **coef):
    num_of_grids = 100
    grid_spacing = (b-a)/num_of_grids
    list_of_values = [a + grid_spacing]
    for i in range(num_of_grids-2):
        list_of_values.append(list_of_values[-1] + grid_spacing)
    list_of_values = [2*fun(i, **coef) for i in list_of_values]
    list_of_values.append(fun(a, **coef)+fun(b, **coef))
    return (b-a)/(2*num_of_grids) * sum(list_of_values)


# quadratic with closure/partial


def quadratic_2(A, B, C):
    coef = (A, B, C)  # is this necessary? couldn't get it to work without it

    def solve_quadratic(x, *coef):
        return A * x**2 + B * x + C
    return solve_quadratic

partial_quadratic_1_3_2 = partial(quadratic, A=1, B=3, C=2)


# Dynamic version


def dynamic_trapz(fun, a, b, num_of_grids=100):
    # num_of_grids = 100
    grid_spacing = (b-a)/num_of_grids
    # return grid_spacing
    list_of_values = [a + grid_spacing]
    for i in range(num_of_grids-2):
        list_of_values.append(list_of_values[-1] + grid_spacing)
    # return list_of_values
    list_of_values = [2*fun(i) for i in list_of_values]
    list_of_values.append(fun(a)+fun(b))
    return (b-a)/(2*num_of_grids) * sum(list_of_values)
