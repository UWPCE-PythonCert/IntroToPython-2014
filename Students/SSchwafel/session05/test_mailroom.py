#!/usr/bin/python

from mailroom_list_comprehensions import *

#dir(mailroom_list_comprehensions) 

def test():
    assert is_name_present('clark kent') == True 
    assert donation_amount('clark kent') == donors['clark kent']

    #I can tell how to test the return values of functions, but I'm not sure how to write tests that do anything else...
    #For example, most of my functions involve user input and not all return something. How would I test these?
