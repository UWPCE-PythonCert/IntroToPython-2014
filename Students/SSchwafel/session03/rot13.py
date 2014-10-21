#!/usr/bin/python
user_string = raw_input("Please enter the string you'd like to encrypt/decrypt with Rot13 ")


#Take a user string

def rot13(x):
    """Takes a letter and moves forward 13 characters"""

    x = int(ord(x))

    if x < 65:
        return chr(x)
        #return ''

    elif x >= 65 and x<=90:

        x = x + 13

        if x > 90:
            x = x - 26
        return chr(x)

    elif x >= 97 and x <= 122:
	x = x + 13
        if x > 122:
            x = x - 26

        return chr(x)

        #x = (x - 122) + 97


user_string = list( user_string )

user_string = ''.join(rot13(x) for x in user_string)

print user_string
