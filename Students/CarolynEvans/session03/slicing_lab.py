__author__ = 'carolyn.evans'

def Slice(seq, task):
    """ This function performs a variety of slicing operations based on the given task parameter.

    :param seq: Parameter 'seq' is the ordered sequence of objects to be sliced.
    :param task: Parameter 'task' designates which slicing operation to perform.
                 Valid values are:
                     swapfirstlast: exchanges first and last objects.
                     removeeveryother: removes every other object.
                     removefirstlastfour: removes the first and last four objects.
                     reverse: reverses the sequence of objects.
                     reorder: change the order of the objects to middle, last, first.
    :return:  The revised sequence.
              If the sequence is too short for the requested task, the sequence is returned unaltered.
    """

    if task == 'swapfirstlast' and len(seq) >= 2:
        seq = seq[-1:] + seq[1:-1] + seq[:1]

    elif task == 'removeeveryother':
        seq = seq[::2]

    elif task == 'reverse':
        seq = seq[::-1]

    elif task == 'reorder':
        onethird = (len(seq) / 3)
        remainder = (len(seq) % 3)
        seq = seq[onethird:onethird*2] + seq[0:onethird] + seq[(onethird + remainder) * -1:]

    elif task == 'removefirstlastfoureveryother':
        seq = Slice(seq[4:-4], 'removeeveryother')


    return seq

# test tuples
assert Slice(tuple(range(9)), 'swapfirstlast') == (8, 1, 2, 3, 4, 5, 6, 7, 0)
assert Slice(tuple(range(9)), 'removeeveryother') == (0, 2, 4, 6, 8)
assert Slice(tuple(range(9)), 'removefirstlastfour') == (0, 1, 2, 3, 4, 5, 6, 7, 8)
assert Slice(tuple(range(9)), 'reverse') == (8, 7, 6, 5, 4, 3, 2, 1, 0)
assert Slice(tuple(range(20)), 'removefirstlastfoureveryother') == (4, 6, 8, 10, 12, 14)
assert Slice(tuple(range(9)), 'reorder') == (3, 4, 5, 0, 1, 2, 6, 7, 8)
# test lists
assert Slice(list(range(9)), 'swapfirstlast') == [8, 1, 2, 3, 4, 5, 6, 7, 0]
assert Slice(list(range(9)), 'removeeveryother') == [0, 2, 4, 6, 8]
assert Slice(list(range(9)), 'removefirstlastfour') == [0, 1, 2, 3, 4, 5, 6, 7, 8]
assert Slice(list(range(9)), 'reverse') == [8, 7, 6, 5, 4, 3, 2, 1, 0]
assert Slice(list(range(20)), 'removefirstlastfoureveryother') == [4, 6, 8, 10, 12, 14]
assert Slice(list(range(9)), 'reorder') == [3, 4, 5, 0, 1, 2, 6, 7, 8]
# test strings
assert Slice('012345678', 'swapfirstlast') == '812345670'
assert Slice('012345678', 'removeeveryother') == '02468'
assert Slice('012345678', 'removefirstlastfour') == '012345678'
assert Slice('012345678', 'reverse') == '876543210'
assert Slice('0123456789abcd', 'removefirstlastfoureveryother') == '468'
assert Slice('0123456789a', 'reorder') == '3450126789a'

print 'All tests passed'

