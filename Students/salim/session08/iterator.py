#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop, *args):
        self.step = 1
        if not args:
            self.start = -1
            self.stop = stop
        else:
            self.start = stop - 1
            self.stop = args[0]
            if len(args) == 2:
                self.step = args[1]
                self.start = stop - self.step

    def __iter__(self):
        self.current = self.start
        return self

    def next(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

if __name__ == "__main__":

    print "Testing the iterator"
    for i in IterateMe_1():
        print i
