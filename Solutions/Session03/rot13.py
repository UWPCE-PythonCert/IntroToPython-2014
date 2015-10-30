#!/usr/bin/env python

"""
A simple function to compute rot13 encoding

ROT13 encryption

Applying ROT13 to a piece of text merely requires examining its alphabetic
characters and replacing each one by the letter 13 places further along in
the alphabet, wrapping back to the beginning if necessary
"""

# note: the string translate() method would be the high-performance solution

# the string module has some handy constants.
import string

# a few handy constants:
a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')


def rot13a(text):
    """
    My first solution: brute force
    """
    # loop through the letters in the input string
    new_text = []
    for c in text:
        # do upper and lower case separately
        if c in string.ascii_lowercase:
            o = ord(c) + 13
            if o > z:
                o = a-1 + o-z
        elif c in string.ascii_uppercase:
            o = ord(c) + 13
            if o > Z:
                o = A-1 + o-Z
        else:
            o = ord(c)
        new_text.append(chr(o))
    return "".join(new_text)


def rot13b(text):
    """
    A little smarter to use % to take care of the wrap-around

    And do a check on the ord value, rather than looking in
    string.ascii_lowercase
    """
    # loop through the letters in teh input string
    new_text = []
    for c in text:
        o = ord(c)
        # do upper and lower case separately
        if a <= o <= z:
            o = a + ((o - a + 13) % 26)
        elif A <= o <= Z:
            o = A + ((o - A + 13) % 26)
        new_text.append(chr(o))
    return "".join(new_text)

# Translation table for 1 byte string objects:
# Faster if you build a translation table and use that


# build a translation table:
str_table = []
# loop through all possible ascii values
for c in range(z+1):  # only need up to z
    # do upper and lower case separately
    if a <= c <= z:
        c = a + (c - a + 13) % 26
    elif A <= c <= Z:
        c = A + (c - A + 13) % 26
    str_table.append(chr(c))
str_table = "".join(str_table)


#   Unicode has a LOT of code points, so better to use a dict
#   and only specifiy the ones that need changing -- in a dict
# NOTE: we haven't covered dicts yet, but for completelness' sake,
#       it's here.

dict_table = {}
# the lower-case letters
for c in range(a, z+1):
    dict_table[c] = a + (c - a + 13) % 26
# the lower-case letters
for c in range(A, Z+1):
    dict_table[c] = A + (c - A + 13) % 26

# OR use the maketrans() method, and hard code the translation
orig =    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotated = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
table = str.maketrans(orig, rotated)


def rot13c(text):
    """
    This one uses str.translate() or unicode.translate()
    """
    return text.translate(str_table)


def rot13d(text):
    """
    this one uses a dict translation table -- so better suite to unicode
    """
    return text.translate(dict_table)


def rot13e(text):
    """
    this one uses a dict translation table -- so better suite to unicode
    """
    return text.translate(dict_table)


import codecs
def rot13f(text):
    """
    This one "cheats" by using the built-in 'rot13' encoding
    """
    return codecs.encode(text, encoding='rot13')


if __name__ == "__main__":
    print (rot13a("Zntargvp sebz bhgfvqr arne pbeare"))
    print (rot13b("Zntargvp sebz bhgfvqr arne pbeare"))
    print (rot13c("Zntargvp sebz bhgfvqr arne pbeare"))
    print (rot13d("Zntargvp sebz bhgfvqr arne pbeare"))
    print (rot13e("Zntargvp sebz bhgfvqr arne pbeare"))
    print (rot13f("Zntargvp sebz bhgfvqr arne pbeare"))


    assert (rot13a("Zntargvp sebz bhgfvqr arne pbeare") ==
            "Magnetic from outside near corner")

    # rot13 should be reversible:
    text = "Some random text to try!"
    assert rot13a(rot13a(text)) == text

    # they all should do the same thing
    assert (rot13a(text) ==
            rot13b(text) ==
            rot13c(text) ==
            rot13d(text) ==
            rot13e(text) ==
            rot13f(text)
            )

    print ("All assertions pass")

# # Some timings:
# # Note that the translate tabel versions are MUCH faster

# In [2]: timeit rot13a('This is a pretty short string, but maybe long enough to test')
# 10000 loops, best of 3: 31.5 µs per loop

# In [3]: timeit rot13b('This is a pretty short string, but maybe long enough to test')
# 10000 loops, best of 3: 32.5 µs per loop

# In [4]: timeit rot13c('This is a pretty short string, but maybe long enough to test')
# The slowest run took 9.36 times longer than the fastest. This could mean that an intermediate result is being cached
# 1000000 loops, best of 3: 1.03 µs per loop

# In [5]: timeit rot13c('This is a pretty short string, but maybe long enough to test')
# The slowest run took 10.23 times longer than the fastest. This could mean that an intermediate result is being cached
# 1000000 loops, best of 3: 1.02 µs per loop

# In [6]: timeit rot13d('This is a pretty short string, but maybe long enough to test')
# The slowest run took 6.75 times longer than the fastest. This could mean that an intermediate result is being cached
# 1000000 loops, best of 3: 1.1 µs per loop

# In [7]: timeit rot13e('This is a pretty short string, but maybe long enough to test')
# The slowest run took 8.59 times longer than the fastest. This could mean that an intermediate result is being cached
# 100000 loops, best of 3: 2.31 µs per loop
