#!/usr/bin/python

"""
example for what happens when you pass non-ascii unicode to a Exception
"""

msg = u'This is an ASCII-compatible unicode message'

#msg = u'This is an non ASCII\N{EM DASH}compatible unicode message'

print "\nDo you see this message in the Exception report?\n"
print msg
print

raise ValueError(msg)

