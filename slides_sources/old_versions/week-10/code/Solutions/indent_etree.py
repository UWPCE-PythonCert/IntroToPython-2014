#!/usr/bin/env python
"""
indenting function to pretty-print an ElementTree

from:

http://infix.se/2007/02/06/gentlemen-indent-your-xml

why the %*#^ this isn't built-in to etree is beyond me.

usage:

indent(tree.getroot())

tree.write(outfilename)

"""

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
            if not e.tail or not e.tail.strip():
                e.tail = i + "  "
        if not e.tail or not e.tail.strip():
            e.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

