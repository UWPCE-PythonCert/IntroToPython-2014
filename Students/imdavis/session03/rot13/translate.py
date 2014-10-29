#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
    Some functions to create a basic substitution cypher.
    Any letter in the alphabet is replaced with the letter 13 spaces away
    The 'rotation' variable can be modified to set the rotation to something
    other than 13. A rotation of 13 makes it such that, you can encrypt and 
    decrypt using these functions, since there are 26 letters in the alphabet.
    This is designed to leave whitespace, punctuation, and capitalization 
    intact in the encrypted string as in the original.

    Lowercase a-z are ordinals 197 -122 (enclusive)
    For example: ord('s') = 115 and chr(115) = 's'

"""

def lowercase(substring):
    """
    Convert a string to lower case so that we only have to deal with 
    the ordinal values for the lowercase letters.
    """
    if(substring.islower()):
        alower = True
    else:
        alower = False
        substring = substring.lower()
    return alower, substring

def encrpt_letter(substring, rot):
    """
    Find the ordinal of the encrypted letter
    """
    letter_pos = ord(substring) + rot
    if(letter_pos > 122):
        letter_pos = 97 + (letter_pos%122 - 1)
    return chr(letter_pos)

def rot13(user_string):
    """
    Take the user string and create the encrypted string
    """
    cipher_string = ""
    rotation=13
    atoz_range = range(97, 123)
    for aletter in user_string:
        lower, aletter = lowercase(aletter)
        if( ord(aletter) in atoz_range):
            cipher_letter = encrpt_letter(aletter, rotation)
            if(not lower):
                cipher_letter = cipher_letter.swapcase()
        else:
            cipher_letter = aletter
        cipher_string += cipher_letter
    return cipher_string

# Some basic testing 
if __name__ == '__main__':
    teststring1 = "Magnetic from outside near corner"
    teststring2 = "Zntargvp sebz bhgfvqr arne pbeare"
    teststring3 = "A string of some stuff with SOME CAPS and numbers 1, 4, 75, etc. ?#$, yeah!"
    teststring4 = "N fgevat bs fbzr fghss jvgu FBZR PNCF naq ahzoref 1, 4, 75, rgp. ?#$, lrnu!"
    try:
        assert rot13(teststring1) == teststring2
        assert rot13(teststring2) == teststring1
        assert rot13(teststring3) == teststring4
        assert rot13(teststring4) == teststring3

    except AssertionError:
        print "Tests did not pass!"