#!/usr/bin/env python2.7

from translate import rot13

astring = raw_input("Enter a string to encrypt > ")
encrypted_string = rot13(astring)

print "Original string:", astring
print "Encrypted string:", encrypted_string