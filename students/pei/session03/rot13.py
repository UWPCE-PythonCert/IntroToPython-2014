"""
The ROT13 encryption scheme is a simple substitution cypher 
where each letter in a text is replace by the letter 13 away from it 
(imagine the alphabet as a circle, so it wraps around).
"""
import string 
rot13 = str.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
str.translate("Zntargvp sebz bhgfvqr arne pbeare", rot13)

#Testing
assert (str.translate("hi", rot13) == "uv")
assert (str.translate("hi", rot13) != "UV")

#Print the result
print (str.translate("Zntargvp sebz bhgfvqr arne pbeare", rot13))

#easy way to do it
#import codecs
#codecs.encode('foobar', 'rot_13')