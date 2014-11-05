"""
lambdalab.py
"""


def function_builder(numrng):
    list = [lambda n, i=n: n + i for n in range(numrng)]
    return list

