#!/usr/bin/python

def count_evens(nums):

    test = [i for i in nums if i % 2 == 0 and i > 0]
    return len(test)

print count_evens(range(20))
