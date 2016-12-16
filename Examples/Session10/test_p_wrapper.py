#!/usr/bin/env python

"""
test code for the p_wrapper assignment
"""

from p_wrapper import p_wrapper, tag_wrapper


def test_p_wrapper():
    @p_wrapper
    def return_a_string(string):
        return string

    assert return_a_string('this is a string') == '<p> this is a string </p>'

def test_with_args():
    @p_wrapper
    def f_string(a, b, this=45 ):
        return "the numbers are: {}, {}, {}".format(a,b,this)

    assert f_string(2, 3, this=54) == "<p> the numbers are: 2, 3, 54 </p>"


# #Extra credit:

def test_tag_wrapper():
    @tag_wrapper('html')
    def return_a_string(string):
        return string

    assert return_a_string("this is a string") == "<html> this is a string </html>"

def test_tag_wrapper2():
    @tag_wrapper('div')
    def return_a_string(string):
        return string

    assert return_a_string("this is a string") == "<div> this is a string </div>"
