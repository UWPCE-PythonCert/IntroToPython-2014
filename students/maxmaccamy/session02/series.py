def fibonacci(n):
    """This function evaluates the nth value of the
    of the fibonacci sequence passed thru the argument n.
    """
    if (n < 0):
        return 0
    elif (1 == n):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    # run some tests
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    print("All tests passed\n")
