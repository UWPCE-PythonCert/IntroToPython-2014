__author__ = 'ryan.morin'

def fibonacci(n):
    """
    :param n: An interger that describes the element of the fibonacci sequence to be returned
    :return: The number that corresponds to the sequence
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    """
    :param n: An interger that describes the element of the lucas sequence to be returned
    :return: The number that corresponds to the sequence
    """
    if n < 1:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)

def sum_series(elmnt, op1=0, op2=1):
    """
    :param elmnt: An interger that describes the element of the specific sequence to be returned
    :param op1: first number in the series
    :param op2: second number in the series
    :return: The number that corresponds to the sequence
    """
    lst = [op1, op2]
    if op1 == 2 and op2 == 1:
        return lucas(elmnt)
    elif op1 == 0 and op2 == 1:
        return fibonacci(elmnt)
    else:
        if elmnt == 0:
            return 0
        elif elmnt == 1:
            return op1
        else:
            for i in range(elmnt):
                temp = lst[i+1] + lst[i]
                lst.append(temp)
        return lst[elmnt-1]

assert (sum_series(0,0,1)) == 0
assert (sum_series(3,0,1)) == 1
assert (sum_series(3,2,1)) == 3
assert (sum_series(3,2,5)) == 7




