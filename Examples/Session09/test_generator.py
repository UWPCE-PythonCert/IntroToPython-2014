"""
test_generator.py

tests the solution to the generator lab

can be run with py.test or nosetests
"""

import generator_solution as gen


def test_intsum():

    g = gen.intsum()

    assert g.next() == 0
    assert g.next() == 1
    assert g.next() == 3
    assert g.next() == 6
    assert g.next() == 10
    assert g.next() == 15


def test_intsum2():

    g = gen.intsum2()

    assert g.next() == 0
    assert g.next() == 1
    assert g.next() == 3
    assert g.next() == 6
    assert g.next() == 10
    assert g.next() == 15


def test_doubler():

    g = gen.doubler()

    assert g.next() == 1
    assert g.next() == 2
    assert g.next() == 4
    assert g.next() == 8
    assert g.next() == 16
    assert g.next() == 32

    for i in range(10):
        j = g.next()

    assert j == 2**15


def test_fib():
    g = gen.fib()

    assert g.next() == 1
    assert g.next() == 1
    assert g.next() == 2
    assert g.next() == 3
    assert g.next() == 5
    assert g.next() == 8
    assert g.next() == 13
    assert g.next() == 21


def test_prime():
    g = gen.prime()

    assert g.next() == 2
    assert g.next() == 3
    assert g.next() == 5
    assert g.next() == 7
    assert g.next() == 11
    assert g.next() == 13
    assert g.next() == 17
    assert g.next() == 19
    assert g.next() == 23

