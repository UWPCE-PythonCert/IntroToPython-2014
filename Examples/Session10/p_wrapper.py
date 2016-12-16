#!/usr/bin/env python
"""
p_wrapper decorator
"""


def p_wrapper(function):
    def func(*args, **kwargs):
        string = function(*args, **kwargs)
        string = "<p> {} </p>".format(string)
        return string
    return func


class tag_wrapper:
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, orig_func):
        def func(*args, **kwargs):
            string = orig_func(*args, **kwargs)
            string = "<{tag}> {s} </{tag}>".format(tag=self.tag, s=string)
            return string
        return func
