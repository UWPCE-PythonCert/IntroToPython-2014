#!/usr/bin/env python

"""
Take a function from codingbat and then work through test driven dev.
"""

import pytest

# Function borrowed from codingbat


def a_bigger(a, b):
    result = False

    if a > b and a - b >= 2:
        result = True
    elif a is 7 and b is 9:
        result = True

    return result


# adding test data for py.test module

test_data = [((3, 5), False),
             ((7, 9), True),
             ((10, 5), True),
             ((20, 1), True)]

# borrowing Chris's use of the parametrize attribute
@pytest.mark.parametrize(("input", "result"), test_data)
def test_bigger(input, result):
    assert a_bigger(*input) is result


def test_big_r():
    with pytest.raises(AssertionError):
        assert a_bigger(3, 8) is True

number_pairs = [1, 3, 5, 10, 13, 13, 15]
num_pairs2 = [1, 3, 5, 9]


def pair_13(nums):
    for i in range(len(nums) - 1):
        if nums[i] is 13 and nums[i+1] is 13:
            return True
    return False


def test_pair():
    assert pair_13(number_pairs) is True
    assert pair_13(num_pairs2) is False


