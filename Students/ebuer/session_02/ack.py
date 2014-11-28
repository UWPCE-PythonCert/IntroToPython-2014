def ack(m, n):
    """Perfom Ackermann function calculation.

    Syntax: ack(m, n)

    Arguments:
    m -- a positive integer
    n -- a positive integer
    Function will return "none" if a negative argument is passed.

    When run in __main__ namespace function will test several
    primary inputs to ensture correct function. Passage of all
    tests will generate a pass message.

    Note: the Ackermann function is very computationally intensive
    and will flood most desktop computers' available RAM for (m, n)
    greater than (3, 4).
    """
    if m < 0 or n < 0:
        return None
    elif not m:
        return n + 1
    elif not n:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

if __name__ == "__main__":
    assert ack(0, 0) == 1
    assert ack(1, 0) == 2
    assert ack(2, 0) == 3
    assert ack(3, 0) == 5
    assert ack(4, 0) == 13
    assert ack(3, 4) == 125
    print "\nAll tests pass.\nCongratulations, you've done it again Mr. Wayne."
