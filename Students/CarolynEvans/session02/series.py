__author__ = 'carolyn.evans'

def fibonacci(n):
    """ This is the Fibonacci Function.
        It is a series of numbers that is seeded with 0 and 1, and then each subsequent
        number in the series is the sum of the prior two numbers.

    :param n: Parameter n designates which value in the fibonacci series to return.
    :return:  An integer from the fibonacci series based on the given n is returned.
              If a negative number is supplied as n, the function returns None.
    """

    import sys

    try:
        if n < 0:
            return None

        if n <= 1:
            return n

        return fibonacci(n-1)+fibonacci(n-2)

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return None


def lucas(n):
    """ This is the Lucas Function.
        It is a series of numbers that is seeded with 2 and 1, and then each subsequent
        number in the series is the sum of the prior two numbers.

    :param n: Parameter n designates which value in the lucas series to return.
    :return:  An integer from the lucas series based on the given n is returned.
              If a number less than 1 is supplied as n, the function returns None.
    """

    import sys

    try:
        if n < 0:
            return None

        if n == 0:
            return 2

        if n == 1:
            return 1

        return lucas(n-1)+lucas(n-2)

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return None


def sum_series(n, firstValue = 0, secondValue = 1):
    """ This function produces a number from a series of numbers that is seeded with
        firstValue and secondValue parameters, and then each subsequent number is the
        sum of the previous two numbers.

    :param n: Parameter n designates which value in the series to return.
    :param firstValue: This is the first value in the series.
    :param secondValue: This is the second value in the series.
    :return:  An integer from the a series based on the given parameters is returned.
    """

    import sys

    try:
        if n < 0:
            return None

        if n == 0:
            return firstValue

        if n == 1:
            return secondValue

        return sum_series(n-1, firstValue, secondValue)+sum_series(n-2, firstValue, secondValue)

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return None


if __name__ == "__main__":
    # test cases for fibonacci()
    assert fibonacci(-1) == None
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # test cases for lucas()
    assert lucas(-1) == None
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # test cases for sum_series
    assert sum_series(0, 0, 1) == 0 #fibonacci 1
    assert sum_series(1, 0, 1) == 1 #fibonacci 2
    assert sum_series(2, 0, 1) == 1 #fibonacci 3
    assert sum_series(3, 0, 1) == 2 #fibonacci 4
    assert sum_series(0, 2, 1) == 2 #lucas 1
    assert sum_series(1, 2, 1) == 1 #lucas 2
    assert sum_series(2, 2, 1) == 3 #lucas 3
    assert sum_series(3, 2, 1) == 4 #lucas 4
    assert sum_series(0, 3, 2) == 3 #other 4
    assert sum_series(1, 3, 2) == 2 #other 4
    assert sum_series(2, 3, 2) == 5 #other 4
    assert sum_series(3, 3, 2) == 7 #other 4

    # throw a whole bunch of random stuff at sum_series
    for n in range (0, 4, 1):
        for firstValue in range (0, 4, 1):
            for secondValue in range (0, 4, 1):
                print n, firstValue, secondValue, sum_series(n, firstValue, secondValue)

    print 'All Tests Passed'