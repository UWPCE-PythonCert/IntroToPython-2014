#!/usr/bin/env python

"""
port of the random unit tests from the python docs to py.test
"""

import random
import pytest


<<<<<<< HEAD
seq = range(10)
=======
seq = list(range(10))
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f


def test_shuffle():
    # make sure the shuffled sequence does not lose any elements
    random.shuffle(seq)
<<<<<<< HEAD
    seq.sort()
    print "seq:", seq
    ## expect this to fail -- so we can see the output.
    assert seq == range(10)


def test_shuffle_immutable():
    pytest.raises(TypeError, random.shuffle, (1,2,3) )
=======
    # seq.sort()  # this will amke it fail, so we can see output
    print("seq:", seq)  # only see output if it fails
    assert seq == list(range(10))


def test_shuffle_immutable():
    pytest.raises(TypeError, random.shuffle, (1, 2, 3))
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f


def test_choice():
    element = random.choice(seq)
    assert (element in seq)


def test_sample():
    for element in random.sample(seq, 5):
        assert element in seq


def test_sample_too_large():
    with pytest.raises(ValueError):
        random.sample(seq, 20)
