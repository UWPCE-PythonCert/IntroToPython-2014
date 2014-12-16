#!/usr/bin/env python


def rot13(s):
    return_s = ''

    # loop through letters in text and encrypt
    for letter in s:

        # encrpyt alphabet characters
        if letter.isalpha():
            if letter.islower():
                return_s += encrypt(letter, 97)
            else:
                return_s += encrypt(letter, 65)

        # do not encrypt non-alphabet characters
        else:
            return_s += str(letter)

    return return_s


def encrypt(letter, start):
    # if letter is in the first 1/2 of the alphabet
    if ord(letter) <= (start + 12):
        return chr(ord(letter) + 13)
    # if letter is in the second 1/2 of the alphabet
    else:
        return chr(ord(letter) - 13)


if __name__ == '__main__':
    assert rot13('Hello') == 'Uryyb'
    assert rot13('HELLO') == 'URYYB'
    assert rot13('hello') == 'uryyb'
