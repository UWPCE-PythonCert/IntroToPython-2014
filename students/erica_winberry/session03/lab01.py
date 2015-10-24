# return a sequence with the first and last items exchanged.
def first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]
    # NOTE: remember to make slices a sequence, not just an index!

assert first_last("kibble") == "eibblk"

# return a sequence with every other item removed
def every_other(seq):
    return seq[::2]

assert every_other("kibble") == "kbl"

# return a sequence with the first and last 4 items removed, and every other item in between
def fl4_skips(seq):
    return seq[4:-4:2]

assert fl4_skips(tuple(range(10))) == (4,)
assert fl4_skips("thequickbrownfox") == "ucbo"

# return a sequence reversed (just with slicing)
def reverse_it(seq):
    return seq[::-1]

assert reverse_it("kibble") == "elbbik"

# return a sequence with the middle third, then last third, then the first third in the new order
def thirds(seq):
    seq_third = int(len(seq) / 3)
    return seq[seq_third:-seq_third] + seq[-seq_third:] + seq[:seq_third]

assert thirds("kibble") == "bbleki"