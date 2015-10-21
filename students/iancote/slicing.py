def swapfirstlast(n):
    """ Return sequence with first and last objects swapped. """
    return n[-1] + n[1:-1] + n[0]

def removeodditems(n):
    """ Return sequence with every other item removed. """
    return n[::2]

def rmfirstlast4andodd(n):
    """ Return a sequence with first and last 4 removed, and every other item in between """
    return n[4:-4:2]

def reverse(n):
    """ Return sequence reversed """
    return n[::-1]

def thirds(n):
    """ Return a sequence with the middle third, then last third, then the first third in the new order """
    l = int(len(n)/3)  # This likely creates a bug were an item in the seq is omitted
    return n[l:len(n)] + n[:l]
