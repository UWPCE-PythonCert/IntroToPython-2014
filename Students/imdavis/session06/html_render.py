#!/usr/bin/env python

"""
Python class example.
"""


# The start of it all:
# Fill it all in here.
class Element(object):
    indent_spaces = 4
    tag_name = u"<html>"
    # use a list here.
    def __init__(self, content=None):
        self.content = []
    def append(self, new_content):
        if (len(new_content) != 0):
            for word in [new_content]:
                self.content.append(word)
            " ".join(self.content)
    def render(self, file_out, ind=""):
        # amessage = u"this is a message"
        # file_out.write(amessage)
