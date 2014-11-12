__author__ = 'Robert W. Perkins'


from count_evens import ct_evens


def test_null():
    assert ct_evens([]) == 0


def test_onenone():
    assert ct_evens([1]) == 0


def test_oneone():
    assert ct_evens([42]) == 1


def test_manyevens():
    assert ct_evens([2, 1, 5, 7, 8, 80]) == 3


def test_allevens():
    assert ct_evens([2, 4, 6, 8, 10, 12]) == 6


def test_manynone():
    assert ct_evens([1, 3, 5, 7, 9, 11, 13]) == 0


def test_repeats():
    assert ct_evens([1,2,3,2,3,3,4,2,6,6,3,9,7,4,12]) == 8