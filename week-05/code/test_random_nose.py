#!/usr/bin/env python

"""
port of the random unit tests from the python docs to nose/py.test
"""

import random
import nose.tools

seq = range(10)

def test_shuffle():
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(seq)
    seq.sort()
    print seq
    assert seq == range(8)

@nose.tools.raises(TypeError)
def test_shuffle_immutable():
    # should raise an exception for an immutable sequence
    random.shuffle( (1,2,3) )

def test_choice():
    element = random.choice(seq)
    assert (element in seq)

def test_sample():
    for element in random.sample(seq, 5):
        assert element in seq

@nose.tools.raises(ValueError)
def test_sample_too_large():
    random.sample(seq, 20)
