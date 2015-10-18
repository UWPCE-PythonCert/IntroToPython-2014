__author__ = 'Ryan'

def fibonacci(n):
    """
    :param n: number
    :return: a list of nth value in the fibonacci series
    """
    fib_lst = [0,1]
    for i in range(n):
        fib_new = int(fib_lst[i]) + int(fib_lst[i+1])
        fib_lst.append(fib_new)
    return fib_lst[(len(fib_lst)-2)]

def lucas(n):
    """
    :param n: number
    :return: a list of the nth value in the lucas series
    """
    lucas_lst = [2,1]
    for i in range(n):
        lucas_new = int(lucas_lst[i]) + int(lucas_lst[i+1])
        lucas_lst.append(lucas_new)
    return lucas_lst[(len(lucas_lst)-2)]

def sum_series(elmnt, op1=0, op2=1):
    """
    :param elmnt: number
    :param op1:  optional variable sequence start value - default equal to zero
    :param op2: optional variable sequence start value - default equal to one
    :return: return the nth value in a series depending on the optional parameters
    """
    lst = [op1, op2]
    for i in range(elmnt):
        num_new = int(lst[i]) + int(lst[i+1])
        lst.append(num_new)
    return lst[(len(lst)-2)]

assert sum_series(5)
assert sum_series(5,2,1)
assert sum_series(5,4,8)