#!/usr/bin/env python

"""
Test code for generator assignments

Designed to be run wioth py.test -- probably would run with nose, too

"""

import generator_solution as gs


def test_intsum():
    g = gs.intsum()
    for val in [0, 1, 3, 6, 10]:
        assert next(g) == val


def test_intsum2():
    g = gs.intsum2()
    for val in [0, 1, 3, 6, 10]:
        assert next(g) == val


def test_doubler():
    g = gs.doubler()
    for val in [1, 2, 4, 8, 16, 32, 64]:
        assert next(g) == val


def test_fib():
    g = gs.fib()
    for val in [1, 1, 2, 3, 5, 8, 13, 21, 34]:
        assert next(g) == val


def test_prime():
    g = gs.prime()
    for val in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
        assert next(g) == val
