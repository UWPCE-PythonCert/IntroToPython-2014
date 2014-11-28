"""
The ROT13 encryption scheme is a simple substitution cypher where each letter in
a text is replace by the letter 13 away from it (imagine the alphabet as a circle,
so it wraps around).

This function should preserve whitespace, punctuation and capitalization.
"""

def rot13():
    from string import maketrans
    intab = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    outtab = "NnOoPpQqRrSsTtUuVvWwXxYyZzAaBbCcDdEeFfGgHhIiJjKkLlMm"
    trantab = maketrans(intab, outtab)          # Required to call maketrans function.

    str1 = "Zntargvp sebz bhgfvqr arne pbeare"
    return str1.translate(trantab)
    # the return is 'Magnetic from outside near corner'

if __name__ == "__main__":
    # execute only if run as a script
    main()

