#!/usr/bin/env python

"""
Simple iterator examples -- now modified by classroom excercises
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like xrange(4) )
    """
    def __init__(self, stop, *args):  # takes stop + optional number of add'l args
        if not args:
            self.current = -1
            self.stop = stop
        else: # when passed a non-empty tuple
            self.current = stop - 1
            self.stop = args[0]

            if len(args[1]) == 2: # check for step argument
                self.step = args[1]
                self.start = stop - self.step

    def __iter__(self):  # returns iterator but also prepares it
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

