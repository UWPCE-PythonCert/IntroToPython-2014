#!/usr/bin/python

# rot13 cypher module


x = input("Input string:  ")

def rot13(x):
    ''' Rot13 encoder/decoder:
            create an empty string called 'code', append characters to 
            it as they're decrptyed (temporarily stored in 'a')
    '''
    code = '' # decoded text aggregator
    for i in x:
        if i in 'abcdefghijklm':
            a = ord(i)+13
            a = chr(a)
            code += a
        elif i in 'nopqrstuvwxyz':
            a = ord(i)-13
            a = chr(a)
            code += a
        elif i in 'ABCDEFGHIJKLM':
            a = ord(i)+13
            a = chr(a)
            code += a
        elif i in 'NOPQRSTUVWXYZ':        
            a = ord(i)-13
            a = chr(a)
            code += a
        else:
            code += i
    return(code)

print(rot13(x))

if __name__ == '__main__':
    assert rot13('bob') == 'obo'
    assert rot13('Zntargvp sebz bhgfvqr arne pbeare')  == 'Magnetic from outside near corner'
