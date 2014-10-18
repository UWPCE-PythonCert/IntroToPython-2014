#!/usr/bin/python
user_string = raw_input("Please enter the string you'd like to decrypt with Rot13")


#Take a user string
def rot13(x):
    """Takes a string and moves each letter forward 13 characters"""
    x = list(x)
    string_ascii_value = []
    for i in x:
        x = ord(x)
        string_ascii_value.append(x)
        
    print x
        #do some rot13 decrypting here


rot13(user_string)
