__author__ = 'Robert W. Perkins'


def ct_evens(in_list):
    """Return number of even ints in the given array"""
    return len([evens for evens in in_list if evens % 2 == 0])

#if __name__ == '__main__':
    #print ct_evens([1,2,3,4,5,6])