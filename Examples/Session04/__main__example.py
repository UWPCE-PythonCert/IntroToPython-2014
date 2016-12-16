#!/usr/bin/env python

print("every module has a __name__")

print("What it is depends on how it is used")

print("right now, this module's __name__ is: {}".format(__name__))

# so if you want coce to run only when a module is a top level script,
# you use this clause:
#if __name__ == "__main__":

print("I must be running as a top-level script")
