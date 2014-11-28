'''
Created on Oct 17, 2014

@author: db345c
'''
import string

def rot13(s):
    dt = string.maketrans( 
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .!<>;:'", 
    "NOPQRSTUVWXYZabcdefgjijklmnopqrstuvwxyzABCDEFGHIJKLM .!<>;:'")
    
    return string.translate("Hello World!", dt)

if __name__ == '__main__':
    one = rot13("Zntargvp sebz bhgfvqr arne pbeare")
    two = rot13(one)
    print one
    print two

### Does not work propery