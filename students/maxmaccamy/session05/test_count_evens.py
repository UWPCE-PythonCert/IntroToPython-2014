__author__ = 'Max'

from codingbat import count_evens

def test_list1():
    assert (3 == count_evens([2, 1, 2, 3, 4]))

def test_list2():
    assert (3 == count_evens([2, 2, 0]))

def test_list3():
    assert (0 == count_evens([1, 3, 5]))