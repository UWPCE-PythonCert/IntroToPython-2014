#!/usr/bin/env python

"""
test code for the quadratic function evaluator
"""

import pytest

from quadratic import Quadratic


def test_init():
    q = Quadratic(1,2,3)


def test_evaluate():
    q = Quadratic(1,2,3)

    assert q(3) == 9 + 6 + 3


def test_bad_input():

    with pytest.raises(TypeError):
        q = Quadratic(2,3)

