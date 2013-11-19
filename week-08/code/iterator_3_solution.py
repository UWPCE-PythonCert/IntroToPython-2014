#!/usr/bin/env python

"""
Simple iterator examples
"""

class IterateMe_3(object):
    """
    Almost a replacement for xrange:
   
    Iterate_2 (start, stop, step=1)

    returns the sequence of numbers from start (inclusive) to stop (exclusive),
    skipping every step number
    ( like xrange(start, stop, step) )
    
    This version re-sets itself when used again.
    """
    def __init__(self, start, stop, step=1):
        self.current = self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        self.current = self.start
        return self
    def next(self):
        if self.current < self.stop:
            self.current += self.step
            return self.current
        else:
            raise StopIteration
        
if __name__ == "__main__":
    
    print "Test the usual"
    for i in IterateMe_3(3, 11, 2):
        print i

    print "This one is different when broken out of"
    it = IterateMe_3(3, 11, 2)
    for i in it:
        if i > 8:
            break
        print i

    print "we pick up again from the beginning"
    for i in it:
        print i

