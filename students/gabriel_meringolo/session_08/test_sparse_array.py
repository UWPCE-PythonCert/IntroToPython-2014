from sparse_array import SparseArray


def test_init():
    assert SparseArray(1,2,3)


#def test_array():
#    sa = SparseArray(1,2,3,4,5,0,0,8,0,0,0,0)
#    assert sa == {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 7: 8, 'len': 12}


def test_len():
    sa = sa = SparseArray(1,2,3,4,5,0,0,8,0,0,0,0)
    assert len(sa) == 12