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
    assert my_sparse[4] == my_array[4]

def test_get_zero():
    my_array, my_sparse = set_up()
    assert my_sparse[1] == my_array[1]

def test_set_element_outside():
    """
    if an element is set outside the current size, the array is expanded
    to fit - makes sense for sparse, as yo know the missing values are zero
    """
    sa = SparseArray([1, 0, 2])
    sa[5] = 2
    assert len(sa) == 6
    assert sa == SparseArray([1, 0, 2, 0, 0, 2])

    # add one just on the end
    sa[6] = 10
    assert sa[6] == 10
    assert sa == SparseArray([1, 0, 2, 0, 0, 2, 10])

def test_negative_index():
    my_array, my_sparse = set_up()
    for i in range(1, len(my_array)):
        print(my_sparse[-i])
        assert my_sparse[-i] == my_array[-i]    

def test_negative_index_too_big():
    my_array, my_sparse = set_up()
    with pytest.raises(IndexError):
        my_sparse[-(len(my_array)+1)] # just too big
    with pytest.raises(IndexError):
        my_sparse[-(len(my_array)+10)] # much too big

def test_get_element_not_in_array():
    my_array, my_sparse = set_up()
    with pytest.raises(IndexError):
        my_sparse[14]

def test_eq():
    ## good to define __eq__ early, so you can use it in tests
    sa1 = SparseArray([0, 2, 4, 0, 1])
    sa2 = SparseArray([0, 2, 4, 0, 1])
    sa3 = SparseArray([0, 2, 3, 0, 1])

    assert sa1 == sa2
    assert not sa1 == sa3

def test_eq_list():
    '''should be equal to alist with the same elements'''
    my_array, my_sparse = set_up()

    assert my_sparse == my_array

def test_eq_othertype():
    '''comparing to a non-sequence should return False'''
    my_array, my_sparse = set_up()
    assert not my_sparse == 5

def test_str():
    #str should be different for long array
    my_sparse = SparseArray([2,0,0,3,0,4,0,0,0,0,0,0,3,0,4])
    s = str(my_sparse)
    assert s == "SparseArray of length: 15 with 5 non-zero elements"


def test_repr():
    my_sparse = SparseArray([2,0,0,3,0,4])
    s = repr(my_sparse)
    assert s == "SparseArray([2, 0, 0, 3, 0, 4])"


def test_get_length():
    my_array, my_sparse = set_up()
    assert len(my_sparse) == 14


def test_change_number_in_array():
    my_array, my_sparse = set_up()
    my_sparse[0] = 3
    assert my_sparse[0] == 3
    # make sure others aren't changed
    for i in range(1,len(my_array)):
        assert my_sparse[i] == my_array[i]
    # make sure still same length
    assert len(my_sparse) == len(my_array)

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
    del my_sparse[5]
    # should still be zero, but should have shorter length
    assert my_sparse[5] == 0
    assert len(my_sparse) == 13


def test_delete_last_number():
    my_array, my_sparse = set_up()
    del(my_sparse[13])
    # should get an error
    with pytest.raises(IndexError):
        my_sparse[13]
    assert len(my_sparse) == 13

def test_indices_change():
    my_array, my_sparse = set_up()
    del(my_sparse[3])
    # next index should have changed
    # my_sparse[4] was 3 now
    # my_sparse[3] should be 3
    assert (my_sparse[3] == 3)


def test_append():
    my_array, my_sparse = set_up()
    my_array.append(4)
    my_sparse.append(4)
    assert my_array == my_sparse


# Slicing -- not all that well tested -- there are LOTS of permutations!
def test_get_slice():
    my_array, my_sparse = set_up()
    assert my_sparse[2:4] == my_array[2:4] # all zeros
    assert my_array[3:7] == my_array[3:7] # other values
    assert my_array[-3:] == my_array[-3:] 
    assert my_array[-5:-1] == my_array[-5:-1] 
    assert my_array[::2] == my_array[::2] 


def test_set_slice():
    my_array, my_sparse = set_up()
    my_sparse[2:5] = [2, 3, 4]
    my_array[2:5] = [2, 3, 4]
    assert len(my_array) == len(my_sparse)
    assert my_sparse == my_array


def test_set_slice_wrong_size():
    my_array, my_sparse = set_up()
    with pytest.raises(ValueError):
        my_sparse[2:4] = [2, 3, 4]    
    with pytest.raises(ValueError):
        my_sparse[2:5] = [2, 3]    


def test_set_slice_wrong_type():
    my_array, my_sparse = set_up()
    with pytest.raises(TypeError):
        my_sparse[2:4] = 5    


def test_change_slice():
    my_array, my_sparse = set_up()
    my_sparse[1:3] = [2, 3]
    assert my_sparse[1:3] == [2, 3]

# This is NOT working -- needs to be fixed!
# def test_set_slice_over_end():
#     # this slice goes over the end
#     # it should expand the array to fit
#     my_array, my_sparse = set_up()
#     print(repr(my_sparse))
#     print(len(my_sparse))
#     my_array[12:16] = [2, 3, 4, 5]
#     print(my_array)
#     my_sparse[12:16] = [2, 3, 4, 5]
#     print(repr(my_sparse))
#     assert my_sparse == my_array

