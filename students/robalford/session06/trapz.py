from math import sqrt


def line(x):
    return 5


def a_curve(x):
    return sqrt(x-1)


def another_curve(x):
    return x * 2 + 1


def trapz(fun, a, b):
    num_of_grids = 100  # breaks when you change # of grids
    grid_spacing = (b-a)/num_of_grids
    # return grid_spacing
    list_of_values = [a + grid_spacing]
    while list_of_values[-1] < (b - (grid_spacing*2)):  #this is to account for bad rounding. there must be a better way!
        list_of_values.append(list_of_values[-1] + grid_spacing)
    # list_of_values.pop()
    # return list_of_values
    list_of_values = [2*fun(i) for i in list_of_values]
    list_of_values.append(fun(a)+fun(b))
    return (b-a)/(2*num_of_grids) * sum(list_of_values)
