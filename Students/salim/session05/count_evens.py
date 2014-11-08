#!/usr/local/bin/python


def count_evens(a_list):
    even_list = [x for x in a_list if x % 2 == 0]
    return len(even_list)
