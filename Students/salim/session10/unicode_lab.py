#!/usr/bin/env python

import io
import os


# test printing unicode
print u'this is a snowman:  \u2603'
print u'this is a snowflake:  \u2744'
print u'this is a theta symbol:  \u0398'


# test reading unicode
eat_glass_utf16 = io.open('ICanEatGlass.utf161.txt', encoding='utf-16')
print eat_glass_utf16.read()

eat_glass_utf8 = io.open('ICanEatGlass.utf81.txt', encoding='utf-8')
print eat_glass_utf8.read()

text1_utf32 = io.open('text1.utf32' ,encoding='utf-32')
print text1_utf32.read()

text1_utf16 = io.open('text1.utf16' ,encoding='utf-16')
print text1_utf16.read()

text1_utf8 = io.open('text1.utf8' ,encoding='utf-8')
print text1_utf8.read()


# test writing/reading unicode to files
try:
    pwd = os.path.dirname(__file__)
except NameError:
    pwd = os.getcwd()

s = u"""
This is a unicode object.  You can tell because I have a bunch of unicode
characters.  Here are some examples:
\t\u06B4
\t\u08A9
\t\u0A74
Isn't that cool!
"""

with io.open(os.path.join(pwd, 'output_test.txt'), 'w') as f:  # io packagge
    f.write(s)

with open(os.path.join(pwd, 'output_test_2.txt'), 'w') as f:  # built in open
    f.write(s.encode('utf-8'))  # must encode before writing
