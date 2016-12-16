#!/usr/bin/env python

"""
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of cigars.

Return True if the party with the given values is successful,
or False otherwise.
"""


# you can change this import to test different versions
from cigar_party import cigar_party
# from cigar_party import cigar_party2 as cigar_party
# from cigar_party import cigar_party3 as cigar_party


def test_1():
    assert cigar_party(30, False) is False


def test_2():

    assert cigar_party(50, False) is True


def test_3():

    assert cigar_party(70, True) is True


def test_4():
    assert cigar_party(30, True) is False


def test_5():
    assert cigar_party(50, True) is True


def test_6():
    assert cigar_party(60, False) is True


def test_7():
    assert cigar_party(61, False) is False


def test_8():
    assert cigar_party(40, False) is True


def test_9():
    assert cigar_party(39, False) is False


def test_10():
    assert cigar_party(40, True) is True


def test_11():
    assert cigar_party(39, True) is False

