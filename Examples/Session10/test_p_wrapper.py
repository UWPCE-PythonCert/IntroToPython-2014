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

#Extra credit:

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
