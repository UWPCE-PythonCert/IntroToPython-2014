#!/usr/bin/env python3



seq = [ 8, 7, 6, 5, 4, 3, 2, 1, "blast", "off"]
seq2 = "Grumpy wizards make toxic brew for the evil Queen and Jack."


def first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]
    

def every_other(seq):
    return seq[::2]


def four_other(seq2):
    return seq[4:-4:2]
    

def reverse(seq):
    return seq[::-1]


def thirds(seq):
    i = len(seq)//3
    return seq[i:-1] + seq[-i:]  + seq[:i] 
    


assert first_last(seq) == [ "off", 4, 3, 2, 1, "blast", 5]
assert every_other(seq) == [ 4, 2, "blast" ] 
assert four_other(seq2) == "py wizards make toxic brew for the evil Queen and J"
assert reverse(seq) == [ "off", "blast", 1, 2, 3, 4, 5 ]
assert thirds(seq) == []