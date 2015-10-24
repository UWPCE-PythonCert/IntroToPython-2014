#!/usr/bin/python

def triple():
    '''Find all words with 3 double letters in a row.  From,
    http://greenteapress.com/thinkpython/html/thinkpython010.html
    http://www.cartalk.com/content/puzzlers  '''
    fin = open('./words.txt')  ## word list to parse
    for word in fin:
        word = fin.readline()
        word = word.strip()
        char = 0
        length = len(word)
        while (char <= length - 6) and (length >=6):
            if word[char] == word[char+1]:
                if word[char+2] == word[char+3]:
                    if word[char+4] == word[char+5]:
                        return(word)
            char+=1

triple()




