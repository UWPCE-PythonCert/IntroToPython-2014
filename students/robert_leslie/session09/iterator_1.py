#!/usr/bin/env python

"""
Simple iterator examples
"""


class IterateMe_1(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """
    def __init__(self, stop=5):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):

        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class IterateMe_2(object):
    """
    About as simple an iterator as you can get:

    iterator_2(start, stop, step=1)

    make it function like range()
    """
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __get_item__(self, position):
        current = self.start + position + self.step
        if current < self.stop:
            return current
        else:
            raise StopIteration


if __name__ == "__main__":

    #print("Testing the iterator")
    #for i in IterateMe_1():
    #    print(i)

    it = IterateMe_2(2, 20, 2)
    for i in it:
        #if i > 10:
        #    break
        print(i)


