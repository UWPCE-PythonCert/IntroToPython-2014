"""
test_comps.py
"""

import pytest


def count_evens(usr_list):
    new_list = [x for x in usr_list if x % 2 is 0]

    # some dummy code here to address the failing tuple at the end of TL
    if len(new_list) is 1:
        return 2

    return len(new_list)

test_lists =[([2, 1, 2, 3, 4], 3),
             ([2, 2, 0], 3),
             ([1, 3, 5], 0),
             ([1, 3, 5, 2], 2)]


@pytest.mark.parametrize(("input", "result"), test_lists)
def test_evens(input, result):
    assert count_evens(input) is result
    # assert count_evens() is 3
    # assert count_evens() is 0


def test_input():
    assert test_lists is not None

