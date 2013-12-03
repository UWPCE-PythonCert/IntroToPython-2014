#!/usr/bin/env python

"""
timer_context

A context manager that does simpel code timing

Adapted from:

http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/


NOTE: this is only good for crude timing -- use the timeit module to do it better.
"""

import time

class Timer(object):    
    def __enter__(self):
        pass
    def __exit__(self, *args):
        pass


if __name__ == "__main__":
    
    # hard to write proper unit tests for this...

    with Timer() as t:
        for i in range(100000):
            i = i**20

    print t.interval







