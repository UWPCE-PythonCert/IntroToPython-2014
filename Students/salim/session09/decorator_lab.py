#!/usr/bin/env python


def p_wrapper(func):
    def wrap(*args, **kwargs):
        tag = kwargs.get('tag', 'p')  # default tag value is <p>
        return '<{}>{}</{}>'.format(tag, args[0].strip(), tag)
    return wrap

@p_wrapper
def return_a_string(string):
    return string

return_a_string('this is my string')
