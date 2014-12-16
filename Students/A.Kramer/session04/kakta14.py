'''
Created on Oct 17, 2014

@author: db345c
'''

import string

def kata14(filename, start):
    """ Set up variables, split lines in the groups of three, populate
        dictionary, and call function to print kata14 """
    # create dictionary    
    words = {}
    # open file
    f = open(filename, "r")
    count = 0
    for line in f:
        # Split the line into separate tokens
        lst = line.split()
        
        # discard all the lines containing less than three words
        if len(lst) > 2:
            
            # Remove punctuation with string.punctuation (import string)
            for j, k in enumerate(lst):
                lst[j] = k.strip(string.punctuation)
            
            # split the line in the groups of three words
            lst_length = len(lst)
            for idx, i in enumerate(lst):
                # assure the last element of the list is reached, if so, break
                if idx == lst_length - 2:
                    break
                else:
                    # got the three strings to use and add those to the dictionary
                    l = [ (lst[idx] + " " + lst[idx + 1]).strip(), lst[idx + 2].strip()]
                    buildDictionary(l, words)
                    count += 1
    # close file
    f.close()
    
    # print kata14    
    printKata14(words, start)

def buildDictionary(l, words):
    """ Populate the dictionary """
    if l[0] in words:
        words[l[0]].append(l[1])
    else:
        words[l[0]] = [l[1]]
    return words
    
def printKata14(word, start):
    """ Recursively print Kata14 """
    if start in word:
        if len(word[start]) > 0:
            temp = word[start].pop()
            print start, temp,
            printKata14(word, str(start.split()[1]) + " " + temp)
        else:
            return
        
if __name__ == "__main__":
    """ Execute Kata14 algorythm """
    kata14("sherlock.txt", "little use")