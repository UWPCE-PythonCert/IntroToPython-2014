#!/usr/bin/env python

"""
Simple iterator examples
"""

class IterateMe_2(object):
    """
    Almost a replacement for xrange:
   
    Iterate_2(start, stop, step=1)

    returns the sequence of numbers from start (inclusive) to stop (exclusive),
    skipping every step number
    ( like xrange(start, stop, step) )

    """
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self
    def next(self):
        if self.current < self.stop:
            self.current += self.step
            return self.current
        else:
            raise StopIteration
        
if __name__ == "__main__":
    
    print "second version"
    for i in IterateMe_2(0, 5):
        print i

    print "second version with a different start"
    for i in IterateMe_2(4, 7):
        print i

    print "second version with a different step"
    for i in IterateMe_2(2, 20, 2):
        print i

    print "But what if we break out of it:"
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:
            break
        print i

    print "And then pick up again"
    for i in it:
        print i



