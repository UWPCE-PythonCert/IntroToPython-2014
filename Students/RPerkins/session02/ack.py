__author__ = 'Robert W. Perkins'


def ack(m, n):
    """Return the result of the Ackermann function on m and n"""
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

# Testing Block
if __name__ == "__main__":
    assert ack(-1, 2) is None
    assert ack(2, -1) is None
    assert ack(-1, -1) is None
    assert ack(0, 0) == 1
    assert ack(0, 1) == 2
    assert ack(0, 2) == 3
    assert ack(0, 3) == 4
    assert ack(0, 4) == 5
    assert ack(1, 0) == 2
    assert ack(1, 1) == 3
    assert ack(1, 2) == 4
    assert ack(1, 3) == 5
    assert ack(1, 4) == 6
    assert ack(2, 0) == 3
    assert ack(2, 1) == 5
    assert ack(2, 2) == 7
    assert ack(2, 3) == 9
    assert ack(2, 4) == 11
    assert ack(3, 0) == 5
    assert ack(3, 1) == 13
    assert ack(3, 2) == 29
    assert ack(3, 3) == 61
    assert ack(3, 4) == 125
    #  max recursion depth exceeded after this point
    #assert ack(4, 0) == 2**2**2-3
    #assert ack(4, 1) == 2**2**2**2-3
    #assert ack(4, 2) == (2**65536)-3
    #assert ack(4, 3) == (2**2**65536)-3
    #assert ack(4, 4) == (2**2**2**65536)-3
    print 'All tests passed'