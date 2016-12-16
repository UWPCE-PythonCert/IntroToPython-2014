#!/usr/bin/env python

"""
test file for codingbat module

This version can be run with nose or py.test
"""

from codingbat import sleep_in, monkey_trouble


# tests for sleep_in
def test_false_false():
    assert sleep_in(False, False)


def test_true_false():
    assert not (sleep_in(True, False))


def test_false_true():
    assert sleep_in(False, True)


def test_true_true():
    assert sleep_in(True, True)


# put tests for monkey_trouble here
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def test_monkey_true_true():
    assert monkey_trouble(True, True)

def test_monkey_false_false():
    assert monkey_trouble(False, False)

def test_monkey_true_false():
    assert monkey_trouble(True, False) is False

# more!
