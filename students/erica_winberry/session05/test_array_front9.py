from codingbat import array_front9
# Given an array of ints, return True if one of the first 4 elements
# in the array is a 9. The array length may be less than 4.


def test_9inrange():
    assert array_front9([1, 2, 9, 3, 4])

def test_not_9inrange():
    assert not array_front9([1, 2, 3, 4, 9])

def test_no9():
    assert not array_front9([1, 2, 3, 4, 5])

def test_short_array():
    assert array_front9([1, 2, 9])

def test_short_without9():
    assert not array_front9([1, 2, 3])


# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False