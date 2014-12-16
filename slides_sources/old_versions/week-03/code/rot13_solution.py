#!/usr/bin/enc python

"""
A simple function to compute rot13 encoding

ROT13 encryption

Applying ROT13 to a piece of text merely requires examining its alphabetic
characters and replacing each one by the letter 13 places further along in
the alphabet, wrapping back to the beginning if necessary
"""

## note: the string translate() method would be the high-performance solution

import string

# a few handy constanst:
a = ord('a')
z = ord('z')
A = ord('A')
Z = ord('Z')


def rot13a(text):
    """
    my first solution
    """
    # loop through the letters
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
        new_text.append( chr(o) )
    return "".join(new_text)

def rot13b(text):
    """
    A little smarter to use % to take care of the wrap-around
    
    -thanks, Howard!
    """
    # loop through the letters
    new_text = []
    for c in text:
        # do upper and lower case separately
        if c in string.ascii_lowercase:
            o = a + ( (ord(c) - a + 13)%26 )
        elif c in string.ascii_uppercase:
            o = A + ( (ord(c) - A + 13)%26 )
        else:
            o = ord(c)
        new_text.append( chr(o) )
    return "".join(new_text)

## Faster if you build a translation table and use that
## a translation table needs to be 256 characters long
##  -- all ord vales from 0 to 255

## NOTE: if you didn't discover
front = str(bytearray(range(A)))
translate_upper = str(bytearray(range(A+13,Z+1))) + str(bytearray(range(A,A+13)))
middle = str(bytearray(range(Z+1, a)))
translate_lower = str(bytearray(range(a+13,z+1))) + str(bytearray(range(a,a+13)))
back = str(bytearray(range(z+1, 256)))

# build the whole thing
table = front + translate_upper + middle + translate_lower + back

def rot13c(text):
    """
    just calls .translate()
    """
    return text.translate(table)


print rot13a("Zntargvp sebz bhgfvqr arne pbeare")
print rot13b("Zntargvp sebz bhgfvqr arne pbeare")
print rot13c("Zntargvp sebz bhgfvqr arne pbeare")

## rot13 should be reversible:
print rot13a(rot13b(rot13c(rot13a('This Should be the Same...'))))

# ## and some timings:
# In [2]: timeit rot13a('This is a pretty short string, but maybe long enough to test')
# 10000 loops, best of 3: 52.2 µs per loop
# 
# In [3]: timeit rot13b('This is a pretty short string, but maybe long enough to test')
# 10000 loops, best of 3: 54.7 µs per loop
# 
# In [4]: timeit rot13c('This is a pretty short string, but maybe long enough to test')
# 1000000 loops, best of 3: 482 ns per loop


