
def ack(m,n):
    """Return Ackerman number"""
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

if __name__ == '__main__':
    assert ack(0,4) == 5
    assert ack(1,4) == 6
    assert ack(0,0) == 1
    assert ack(2,2) == 7
    assert ack(3,4) == 125
    assert ack(4,0) == 13
    assert ack(3,2) == 29
    
    print "All Tests Pass"