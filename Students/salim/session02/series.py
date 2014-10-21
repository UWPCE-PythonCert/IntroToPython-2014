#!/usr/env/python


def fibonacci(n):
    """Returns the nth number of the Fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Returns the nth number of the Lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, first=0, second=1):
    """Returns the nth number in the Fibonacci or Lucas seris."""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)


if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18

    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(5) == 5
    assert sum_series(6) == 8
    assert sum_series(7) == 13
    assert sum_series(0, first=2, second=1) == 2
    assert sum_series(1, first=2, second=1) == 1
    assert sum_series(2, first=2, second=1) == 3
    assert sum_series(3, first=2, second=1) == 4
    assert sum_series(4, first=2, second=1) == 7
    assert sum_series(5, first=2, second=1) == 11
    assert sum_series(6, first=2, second=1) == 18
