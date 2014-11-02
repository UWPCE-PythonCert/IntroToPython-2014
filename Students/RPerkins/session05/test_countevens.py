__author__ = 'Robert W. Perkins'


from count_evens import ct_evens


def test_null():
    assert ct_evens([]) is None


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