"""
lambdalab.py
"""


def function_builder(numrng):
    list = [lambda n, i=n: n ** 2 + i for x in range(numrng)]
    return list
