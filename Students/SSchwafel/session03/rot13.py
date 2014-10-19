#!/usr/bin/python
user_string = raw_input("Please enter the string you'd like to decrypt with Rot13 ")


#Take a user string
def rot13(x):
    """Takes a letter and moves forward 13 characters"""

    x = int( ord(x ))
    x = x+13

    if x < 65:
        return ''
    if x >= 65 and x<=90:
        x = chr((x - 90) + 65)

    elif x > 122:
        x = chr((x - 122) + 97)
    print x
        #do some rot13 decrypting here




rot13(user_string)
