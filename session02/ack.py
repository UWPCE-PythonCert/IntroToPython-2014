__author__ = 'carolyn.evans'

def ack(m, n):
    """ This is the Ackermann Function.
    For a complete description, visit en.wikipedia.org/wiki/Ackermann_function.

    :param m: Parameter m must be an integer value of zero or more.
    :param n: Parameter m must be an integer value of zero or more.
    :return:  If m and n are valid, an integer is returned. Otherwise, None is returned.
    """

    import sys
    
    try:
        if m < 0 or n < 0:
            return None

        if m == 0:
            return n+1

        if n == 0:
            return ack(m-1, 1)

        return ack(m-1, ack(m, n-1))
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return None

if __name__ == "__main__":
    for m in range(0, 5, 1):
        for n in range(0, 5, 1):
            print m, n, ack(m, n)