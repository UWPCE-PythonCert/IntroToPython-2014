#!/usr/bin/enc python

"""
A simple function to compute rot13 encoding

ROT13 encryption

Applying ROT13 to a piece of text merely requires examining its alphabetic
characters and replacing each one by the letter 13 places further along in
the alphabet, wrapping back to the beginning if necessary
"""

import string

def rot13a(text):
    # loop through the letters
    new_text = []
    for c in text:
        # do upper and lower case separately
        if c in string.ascii_lowercase:
            o = ord(c) + 13
            if o > ord('z'):
                o = ord('a')-1 + o-ord('z')
        elif c in string.ascii_uppercase:
            o = ord(c) + 13
            if o > ord('Z'):
                o = ord('A')-1 + o-ord('Z')
        else:
            o = ord(c)
        new_text.append( chr(o) )
    return "".join(new_text)

print rot13a("Zntargvp sebz bhgfvqr arne pbeare")
