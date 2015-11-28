from sparse_array import SparseArray


def test_init():
    assert SparseArray(1, 2, 3)


def test_sparse():
    sa = SparseArray(1, 2, 3)
    assert sa.sparse == (1, 2, 3)


def test_array():
    sa = SparseArray(1, 2, 3, 0, 4, 0, 0, 0, 9)
    assert sa.array == {0: 1, 1: 2, 2: 3, 4: 4, 8: 9}


def test_repr():
    sa = SparseArray(1, 2, 3, 4, 5)
    assert repr(sa) == "SparseArray(1, 2, 3, 4, 5)"


def test_str():
    sa = SparseArray(1, 2, 3, 4, 5)
    assert str(sa) == "{0: 1, 1: 2, 2: 3, 3: 4, 4: 5}"


def test_len():
    sa = SparseArray(1, 2, 3, 0, 4, 0, 0, 0, 9)
    assert len(sa) == 9


def test_get():
    sa = SparseArray(1, 2, 3, 4, 5)
    assert sa[1] == 2


def test_set():
    sa = SparseArray(1, 2, 3, 4, 5)
    sa[0] = 2
    assert sa[0] == 2


