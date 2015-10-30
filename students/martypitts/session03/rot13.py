'''
Title: ROT13
Dev: MP
Date: Oct23, 2015
Description:
This module should provide at least one function called rot13 that takes any amount
of text and returns that same text encrypted by ROT13.
This function should preserve whitespace, punctuation and capitalization.

Your module should include an if __name__ == '__main__': block with tests
(asserts) that demonstrate that your rot13 function and any helper functions
you add work properly.

table, such as the following:

Input  ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
Output NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm
Chris =          67 104 114 105 115
Chris + Rot13 =  80 117 127 118 128
Chris (Calc)  =  80 117 127 118



'''

# Encode the values using rot13 algroythm encrypt
def rot13(seq):
    encodestr = []
    asciistr = []
    for i in seq:
        asciival = int(ord(i))
        if asciival > 64 and asciival < 78:
            rot13val = asciival + int(13)
        elif asciival > 77 and asciival < 91:
            rot13val = asciival - int(13)
        elif asciival > 96 and asciival < 110:
            rot13val = asciival + int(13)
        elif asciival > 109 and asciival < 123:
            rot13val = asciival - int(13)
        elif asciival > 31 and asciival < 48:
            rot13val = asciival + int(13)
        asciistr.append(asciival)
        encodestr.append(rot13val)
    # print("The ascii string=", asciistr)
    # print("The rot13 encoded string=", encodestr)

    return encodestr

# Print out the encoded message
def rot13chardump(seq):
    encrypted = []
    for i in seq:
        charval = chr(i)
        encrypted.append(charval)
    # print("The encrpyted message = ", encrypted)
    return encrypted

# Decode the values using rot13 algroythm decrypt
def rot13inv(seq):
    decodestr = []
    asciistr = []
    for i in seq:
        asciival = int(ord(i))
        if asciival > 64 and asciival < 78:
            rot13val = asciival + int(13)
        elif asciival > 77 and asciival < 91:
            rot13val = asciival - int(13)
        elif asciival > 96 and asciival < 110:
            rot13val = asciival + int(13)
        elif asciival > 109 and asciival < 123:
            rot13val = asciival - int(13)
        elif asciival > 31 and asciival < 48:
            rot13val = asciival - int(13)
        asciistr.append(asciival)
        decodestr.append(rot13val)
    # print("The ascii string=", asciistr)
    # print("The rot13 decoded string=", decodestr)
    return decodestr
'''
################################################
# General tests for encrypting decrypting data
################################################
'''

# define the character string
encodestr = 'Chris!'
rot13num = rot13(encodestr)

# dump the encrypted character sting
print("The charter set for encrypted are =", rot13chardump(rot13num), "The charter string =", ''.join(rot13chardump(rot13num)))

# decrypt the character string
decodestr = ''.join(rot13chardump(rot13num))
rot13numinv = rot13inv(decodestr)

# dump the decrypted character string
print("The charter set for encrypted are =", rot13chardump(rot13numinv), "The charter string =", ''.join(rot13chardump(rot13numinv)))

'''
##########################################################
# General assert for encrypting decrypting data verifiation
##########################################################
'''
assert ''.join(rot13chardump(rot13('Chris!'))) == 'Puevf.'
assert ''.join(rot13chardump(rot13('NOPQRSTUVWXYZ'))) == 'ABCDEFGHIJKLM'
assert ''.join(rot13chardump(rot13('ABCDEFGHIJKLM'))) == 'NOPQRSTUVWXYZ'
assert ''.join(rot13chardump(rot13('abcdefghijklm'))) == 'nopqrstuvwxyz'
assert ''.join(rot13chardump(rot13('nopqrstuvwxyz'))) == 'abcdefghijklm'

'''
##########################################################
# Translate the secret ovelteam message
##########################################################
'''
encodestr = 'Zntargvp sebz bhgfvqr arne pbeare'
rot13num = rot13(encodestr)
print("The charter set for encrypted are =", ''.join(rot13chardump(rot13num)))

