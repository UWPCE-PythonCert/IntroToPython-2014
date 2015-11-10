__author__ = 'Max'

from codingbat import cigar_party

def test_thirty_false():
    assert not cigar_party(30, False)

def test_fifty_false():
    assert cigar_party(50, False)

def test_seventy_true():
    assert cigar_party(50, False)
