#!usr/local/bin/python

import sparse_array


def test_len():
    sa = sparse_array.SparseArray([0, 1, 0, 3, 4, 0, 9, 0])
    assert len(sa) == 8

    sa2 = sparse_array.SparseArray([])
    assert len(sa2) == 0

    sa3 = sparse_array.SparseArray((3, 4, 0, 9, 0))
    assert len(sa3) == 5

    sa4 = sparse_array.SparseArray((0, 0, 0, 0, 0))
    assert len(sa4) == 5


def test_get_item():
    sa = sparse_array.SparseArray([0, 1, 0, 3, 4, 0, 9, 0])
    assert sa[0] == 0
    assert sa[1] == 1
    assert sa[2] == 0
    assert sa[3] == 3
    assert sa[4] == 4
    assert sa[5] == 0
    assert sa[6] == 9
    assert sa[7] == 0

    try:
        sa[8]
    except IndexError:
        assert True
    else:
        assert False


def test_set_item():
    sa = sparse_array.SparseArray([0, 0, 4, 100, 0, 3, 9])
    sa[0] = 1
    sa[1] = 0
    sa[2] = 0
    sa[3] = 8

    assert sa[0] == 1
    assert sa[1] == 0
    assert sa[2] == 0
    assert sa[3] == 8
    assert sa[4] == 0
    assert sa[5] == 3
    assert sa[6] == 9

    try:
        sa[8]
    except IndexError:
        assert True
    else:
        assert False


def test_del_item():
    sa = sparse_array.SparseArray([0, 1, 0, 100, 0, 3, 9])

    del sa[0]
    # ([1, 0, 100, 0, 3, 9])
    assert len(sa) == 6
    assert sa[0] == 1
    assert sa[1] == 0
    assert sa[2] == 100
    assert sa[3] == 0
    assert sa[4] == 3
    assert sa[5] == 9

    del sa[4]
    # ([1, 0, 100, 0, 9])
    assert len(sa) == 5
    assert sa[0] == 1
    assert sa[1] == 0
    assert sa[2] == 100
    assert sa[3] == 0
    assert sa[4] == 9

    del sa[1]
    # ([1, 100, 0, 9])
    assert len(sa) == 4
    assert sa[0] == 1
    assert sa[1] == 100
    assert sa[2] == 0
    assert sa[3] == 9

    try:
        del sa[8]
    except IndexError:
        assert True
    else:
        assert False


def test_contains():
    sa = sparse_array.SparseArray([0, 1, 0, 100, 0, 3, 9])

    assert 0 in sa
    assert 1 in sa
    assert 100 in sa
    assert 3 in sa
    assert 9 in sa
    assert not 10 in sa
    assert not 99 in sa


def test_slice():
    sa = sparse_array.SparseArray([0, 1, 0, 100, 0, 3, 9])

    assert sa[0:1] == [0]
    assert sa[1:3] == [1, 0]
    assert sa[1:4] == [1, 0, 100]
    assert sa[2:] == [0, 100, 0, 3, 9]
    assert sa[:4] == [0, 1, 0, 100]
