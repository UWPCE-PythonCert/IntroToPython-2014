"""
test_generator.py

tests the solution to the generator lab

can be run with py.test or nosetests
"""

import generator_solution as gen


def test_intsum():

    g = gen.intsum()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


def test_intsum2():

    g = gen.intsum2()

    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 3
    assert next(g) == 6
    assert next(g) == 10
    assert next(g) == 15


def test_doubler():

    g = gen.doubler()

    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 4
    assert next(g) == 8
    assert next(g) == 16
    assert next(g) == 32

    for i in range(10):
        j = next(g)

    assert j == 2**15


def test_fib():
    g = gen.fib()

    assert next(g) == 1
    assert next(g) == 1
    assert next(g) == 2
    assert next(g) == 3
    assert next(g) == 5
    assert next(g) == 8
    assert next(g) == 13
    assert next(g) == 21


def test_prime():
    g = gen.prime()

    assert next(g) == 2
    assert next(g) == 3
    assert next(g) == 5
    assert next(g) == 7
    assert next(g) == 11
    assert next(g) == 13
    assert next(g) == 17
    assert next(g) == 19
    assert next(g) == 23

