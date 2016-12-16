"""
From codingbat: List2

A student wondered if this execrxise could be done with a generator.

Indeed is can

Return the sum of the numbers in the array, except ignore sections of
numbers starting with a 6 and extending to the next 7 (every 6 will be
followed by at least one 7). Return 0 for no numbers.

sum67([]) → 0
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""


def sum67_loop(nums):
    """
    A basic loop method. the key is to keep a flag
    set to know whether a 6 has been encountered
    """
    total = 0
    is6 = False
    for num in nums:
        print("adding:", num, is6)
        if num == 6 or is6:
            is6 = True
        else:
            total += num
        if num == 7:
            is6 = False
    return total


# to do this with a generator, you need to make a generator function that
# yields the numbers you want added to the sum, and then sum what it produces

# the generator function looks a lot like the one above, but without
# adding the numbers up
def sum67_gen(nums):
    """
    A generator function
    The key is to keep a flag set to know whether a 6 or 7 has been
    encountered, so you know which numbers to yield
    """
    is6 = False
    for num in nums:
        print("adding:", num, is6)
        if num == 6 or is6:
            is6 = True
        else:
            yield num
        if num == 7:
            is6 = False


# tests that will be run by pytest
def test_simple():
    assert sum67_loop([]) == 0
    assert sum67_loop([1, 2, 2]) == 5
    assert sum67_loop([1, 2, 2, 6, 99, 99, 7]) == 5
    assert sum67_loop([1, 1, 6, 7, 2]) == 4


def test_gen():
    """
    you need to call the sum function to use the generator
    """
    assert sum(sum67_gen([])) == 0
    assert sum(sum67_gen([1, 2, 2])) == 5
    assert sum(sum67_gen([1, 2, 2, 6, 99, 99, 7])) == 5
    assert sum(sum67_gen([1, 1, 6, 7, 2])) == 4
