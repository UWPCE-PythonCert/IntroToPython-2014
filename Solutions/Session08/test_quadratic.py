#!/usr/bin/env python

"""
Test code for the quadratic function evaluator

This one uses a callable class, rather than curring functions
"""

import pytest

from quadratic import Quadratic


def test_init():
    q = Quadratic(1,2,3)


def test_evaluate():
    q = Quadratic(1,2,3)

    assert q(3) == 9 + 6 + 3
    assert q(0) == 3


def test_evaluate2():
    q = Quadratic(2,1,-3)

    assert q(0) == -3
    assert q(1) == 2 + 1 - 3
    assert q(-2) == 8 - 2 - 3


def test_bad_input():

    with pytest.raises(TypeError):
        q = Quadratic(2,3)

