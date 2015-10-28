#!/usr/bin/env python3

"""
The version done in class
"""


def swap(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]


assert swap('something') == 'gomethins'
assert swap(tuple(range(10))) == (9, 1, 2, 3, 4, 5, 6, 7, 8, 0)


def rem(seq):
    return seq[::2]

assert rem('a word') == 'awr'


def rem4(seq):
    return seq[4:-4:2]

print(rem4((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), ))


def reverse(seq):
    return seq[::-1]


print(reverse('a string'))


def thirds(seq):
    i = len(seq)//3
    return seq[i:-i] + seq[-i:] + seq[:i]

print (thirds(tuple(range(12))))
