#!/usr/bin/env python

"""
port of the random unit tests from the python docs to py.test
"""

import random
import pytest


seq = range(10)


def test_shuffle():
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(seq)
    seq.sort()
    print "seq:", seq
    ## expect this to fail -- so we can see the output.
    assert seq == range(10)


def test_shuffle_immutable():
    pytest.raises(TypeError, random.shuffle, (1,2,3) )


def test_choice():
    element = random.choice(seq)
    assert (element in seq)


def test_sample():
    for element in random.sample(seq, 5):
        assert element in seq


def test_sample_too_large():
    with pytest.raises(ValueError):
        random.sample(seq, 20)
