# return a sequence with the first and last items exchanged.
def first_last(seq):
    return seq[-1] + seq[1:len(seq)-1] + seq[0]

# return a sequence with every other item removed
def every_other(seq):
    return seq[::2]

# return a sequence with the first and last 4 items removed, and every other item in between
def fl4_skips(seq):
    return seq[4:-4:2]

# return a sequence reversed (just with slicing)
def reversed(seq):
    return seq[::-1]

# return a sequence with the middle third, then last third, then the first third in the new order
def thirds(seq):
    seq_third = len(seq) / 3
    return seq[int(seq_third):-int(seq_third)] + seq[-int(seq_third):] + seq[:int(seq_third)]