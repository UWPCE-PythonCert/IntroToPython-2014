def y_xrange(start, stop, step=1):
    """
    a version of xrange, using a generator
    """
    i = start
    while i < stop:
        yield i
        i += step


def y_xrange_2(start, stop=None, step=1):
    """
    a version of xrange, using a generator
    
    supports the full set of options
    """
    if stop is None:
        stop = start
        start = 0
    i = start
    while i < stop:
        yield i
        i += step




if __name__ == '__main__':
    print "y_xrange(0, 5)"
    for item in y_xrange(0, 5):
        print  item

#    print "y_xrange(-4, 4, 2)"
#    for item in y_xrange(-4, 4, 2):
#        print  item
#
#    print "y_xrange_2(4)"
#    for item in y_xrange_2(4):
#        print  item
#
#    print "y_xrange_2(2, 5)"
#    for item in y_xrange_2(2, 5):
#        print  item
#
#    print "y_xrange_2(10, step=2)"
#    for item in y_xrange_2(10, step=2):
#        print  item

    