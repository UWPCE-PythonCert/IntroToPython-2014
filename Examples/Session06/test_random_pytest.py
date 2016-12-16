#!/usr/bin/env python

"""
port of the random unit tests from the python docs to py.test
"""

import random
import pytest


seq = list(range(10))


def test_shuffle():
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(seq)
    # seq.sort()  # commenting this out will make it fail, so we can see output
    print("seq:", seq)  # only see output if it fails
    assert seq == list(range(10))


def test_shuffle_immutable():
    """should get a TypeError with an imutable type """
    with pytest.raises(TypeError):
        random.shuffle((1, 2, 3))


def test_choice():
    """make sure a random item selected is in the original sequence"""
    element = random.choice(seq)
    assert (element in seq)


def test_sample():
    """make sure all items returned by sample are there"""
    for element in random.sample(seq, 5):
        assert element in seq


def test_sample_too_large():
    """should get a ValueError if you try to sample too many"""
    with pytest.raises(ValueError):
        random.sample(seq, 20)
