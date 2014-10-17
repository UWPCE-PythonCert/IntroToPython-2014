#create a function that encodes/decodes rot13

import string as s

inkey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
outkey = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
complete_key = s.maketrans(inkey, outkey)

test_phrase = 'Zntargvp sebz bhgfvqr arne pbeare'
print test_phrase.translate(complete_key)

#Seems too easy! May try again using extended looping for practice.
