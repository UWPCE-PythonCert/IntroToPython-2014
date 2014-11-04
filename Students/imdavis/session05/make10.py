#!/usr/bin/env python2.7

def make10(a, b):
    """
    Simple function which takes on two arguments and returns 'True' if
    either of them is 10, or their sum is 10.  Returns 'False' otherwise.
    """
    if(a == 10 or b == 10):
        return True
    else:
        try:
            if (a + b == 10):
                return True
            else:
                return False
        except (TypeError):
            print "Sorry, cannot do {0} + {1}".format(a, b)
            return False
