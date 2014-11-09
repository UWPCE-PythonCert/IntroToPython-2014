#!/usr/local/bin/python

from count_evens import count_evens


def test_count_evens_1():
    assert count_evens([2, 1, 2, 3, 4]) == 3


def test_count_evens_2():
    assert count_evens([2, 1, 2, 3, 4]) == 3


def test_count_evens_3():
    assert count_evens([2, 2, 0]) == 3


def test_count_evens_4():
    assert count_evens([1, 3, 5]) == 0


def test_count_evens_5():
    assert count_evens([]) == 0


def test_count_evens_6():
    assert count_evens([11, 9, 0, 1]) == 1


def test_count_evens_7():
    assert count_evens([2, 11, 9, 0]) == 2


def test_count_evens_8():
    assert count_evens([2]) == 1


def test_count_evens_9():
    assert count_evens([2, 5, 12]) == 2
