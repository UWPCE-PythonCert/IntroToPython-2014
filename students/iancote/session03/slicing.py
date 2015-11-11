def swapfirstlast(n):
    """ Return sequence with first and last objects swapped. """
    return n[-1:] + n[1:-1] + n[:1]

assert swapfirstlast("123456") == "623451"
assert swapfirstlast(tuple(range(10))) == (9, 1, 2, 3, 4, 5, 6, 7, 8, 0)


def removeodditems(n):
    """ Return sequence with every other item removed. """
    return n[::2]

assert removeodditems("0123456789") == "02468"


def rmfirstlast4andodd(n):
    """ Return a sequence with first and last 4 removed, and every other item
     in between """
    return n[4:-4:2]


def reverse(n):
    """ Return sequence reversed """
    return n[::-1]


def thirds(n):
    """ Return a sequence with the middle third, then last third, then the
    first third in the new order """
    # This likely creates a bug were an item in the seq is omitted
    l = int(len(n)/3)
    return n[l:] + n[:l]
