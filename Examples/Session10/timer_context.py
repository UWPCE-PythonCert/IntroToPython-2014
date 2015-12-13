#!/usr/bin/env python3

"""
Timer context manager
"""
import time


class Timer:
    def __init__(self, file_like):
        self.file_like = file_like

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, *args):
        elapsed = time.clock() - self.start
        msg = "Elapsed time: {} seconds".format(elapsed)
        self.file_like.write(msg)
        return False
