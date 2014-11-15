__author__ = 'Ari'

import codecs
import sys
import unittest

def rot13(s):
    """Return a letter with a letter 13 letters after it in the alphabet.
    EX: A = N
    Uses the codecs module: https://docs.python.org/2/library/codecs.html#codec-base-classes"""
    return s.encode('rot_13')

def main(input_data):
    print rot13(input_data)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])

        m = "Zntargvp sebz bhgfvqr arne pbeare"
        n = "Magnetic from outside near corner"
        assert rot13(m)==n

    else:
        print 'To use: rot13.py [some string]'
        sys.exit(1)


