import pytest
from sparse_array import SparseArray


def set_up():
    my_array = [2, 0, 0, 0, 3, 0, 0, 0, 4, 5, 6, 0, 2, 9]
    my_sparse = SparseArray(my_array)
    return (my_array, my_sparse)

def test_object_exists():
    my_array, my_sparse = set_up()
    assert isinstance(my_sparse, SparseArray)

def test_get_non_zero_number():
    my_array, my_sparse = set_up()
    assert my_sparse[4] == 3

def test_get_zero():
    my_array, my_sparse = set_up()
    assert my_sparse[1] == 0

def test_get_element_not_in_array():
    my_array, my_sparse = set_up()
    with pytest.raises(IndexError):
        my_sparse[14]

def test_get_lenght():
    my_array, my_sparse = set_up()
    assert len(my_sparse) == 14

def test_change_number_in_array():
    my_array, my_sparse = set_up()
    my_sparse[0] = 3
    assert my_sparse[0] == 3
    # make sure others aren't changed
    assert my_sparse[1] == 0
    # make sure still same length
    assert len(my_sparse) == 14

def test_change_number_in_array_to_zero():
    my_array, my_sparse = set_up()
    my_sparse[4] = 0
    assert my_sparse[4] == 0
    # make sure still same length
    assert len(my_sparse) == 14

def test_change_number_in_array_from_zero():
    my_array, my_sparse = set_up()
    my_sparse[1] = 4
    assert my_sparse[1] == 4
    # make sure still same length
    assert len(my_sparse) == 14

def test_delete_number():
    my_array, my_sparse = set_up()
    del(my_sparse[4])
    # if we delete the 4 position, should now be zero
    assert my_sparse[4] == 0
    # should have smaller length
    assert len(my_sparse) == 13

def test_delete_zero():
    my_array, my_sparse = set_up()
    del(my_sparse[5])
    # should still be zero, but should have shorter length
    assert my_sparse[5] == 0
    assert len(my_sparse) == 13

def test_delete_last_number():
    my_array, my_sparse = set_up()
    del(my_sparse[13])
    # should get an error?
    print 'print some stuff damnit'
    with pytest.raises(IndexError):
        my_sparse[13]
    assert len(my_sparse) == 13



