__author__ = 'Max MacCamy'

def slice1(seq):
    """
    :param seq:
    :return:Sequence with the first and last item of the given seq exchanged.
    """
    return seq[-1:] + seq[1:-1] + seq[:1]

def slice2(seq):
    """
    :param seq:
    :return: Sequence with every other item removed.
    """
    return seq[::2]

def slice3(seq):
    """
    :param seq:
    :return: Sequence with the first and last 4 items removed, and every other
    item in between.
    """
    return seq[4:-4:2]

def slice4(seq):
    """
    :param seq:
    :return: Reverses a sequence
    """
    return seq[::-1]

def slice5(seq):
    """
    :param seq:
    :return: Sequence that is rearranged such that the middle third is returned first,
    then last third, and finally the first third.
    """
    return seq[len(seq)//3:] + seq[:len(seq)//3]

if __name__ == '__main__':
    s = "lets test these functions"
    print(slice1(s))
    print(slice2(s))
    print(slice3(s))
    print(slice4(s))
    print(slice5(s))