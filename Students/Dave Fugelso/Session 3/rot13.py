'''

Dave Fugelso, UW Python Course



'''

import string


def rot13(encrypted):
    '''
    Make a translation table with a rotated alphabet.
    '''
    input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    table = string.maketrans(input, output)
    print encrypted
    print encrypted.translate(table)
    print len(input)
    
    '''
    In case there were ever some unknown rotation length
    #rotate the translation table until we get something that's legible
    for i in range (0, 26):
        output = input[i:26]+input[0:i]+input[i+26:52]+input[26:i+26]
        #print output
        table = string.maketrans(input, output)
        print encrypted.translate(table)
    '''

     

if __name__ == "__main__":
   rot13 ('Zntargvp sebz bhgfvqr arne pbeare')