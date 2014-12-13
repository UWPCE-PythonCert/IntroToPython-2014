#!/usr/local/bin/python

class Element(object):

    def __init__(self, content=None):
        self.content = content
    def append(self, new_content):
        self.content += new_content
    def render(self, file_out, ind=""):
        pass
