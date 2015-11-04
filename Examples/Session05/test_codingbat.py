#!/usr/bin/env python

"""
test file for codingbat module

This version can be run with nose or py.test
"""

from codingbat import sleep_in


def test_false_false():
    assert sleep_in(False, False)


def test_true_false():
<<<<<<< HEAD
    assert not ( sleep_in(True, False) )
=======
    assert not (sleep_in(True, False))
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f


def test_false_true():
    assert sleep_in(False, True)


def test_true_true():
    assert sleep_in(True, True)
