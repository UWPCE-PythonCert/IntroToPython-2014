def ack(m,n):
    """Return results m, input parameter values ranging from 0,0 -4,4 to the Ackermann Function."""    
      
    if m < 0 or n < 0:
        return None
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

if __name__ == '__main__':

    assert ack(-1,0) == None
    assert ack(0,0) == 1
    assert ack(0,1) == 2
    assert ack(0,2) == 3
    assert ack(0,3) == 4
    assert ack(0,4) == 5
    assert ack(1,0) == 2
    assert ack(1,1) == 3
    assert ack(1,2) == 4
    assert ack(1,3) == 5
    assert ack(1,4) == 6

    print "All Tests Pass"

    