__author__ = 'ryan.morin'

import random

com_man_list = []
wrd_list = []
lst = []
temp_list = []
d = dict()

def open_file():
    """
    This function opens a text file.
    :return: The full text file
    """
    orig_doc = open('c:/Users/Ryan/Sherlock.txt', 'r')
    lines = orig_doc.readlines()
    orig_doc.close()
    return lines

def splt(lst):
    """
    This function splits the list into individual words
    :param lst: list
    :return: list of words
    """
    for wrd in lst:
        wrd_lst = (wrd.split())
        com_man_list.append(wrd_lst)
    return (com_man_list)

def str_loop():
    """
    The loop removes special characters from the words
    :return: a list of words that has the special characters removed
    """
    chr_to_repl = ':;()/<>?"'
    for line in splt(open_file()):
        for wrd in line:
            for i in range(0,len(chr_to_repl)):
                wrd = wrd.replace(chr_to_repl[i],'')
            wrd_list.append(wrd)
    return (wrd_list)

def dict_seed():
    """
    This function joins the words i and i+1 adds it to a dictionary and adds i+2 as the dictionary's vakue
    :return: a dictionary with the words from the input file
    """
    l = str_loop()
    for i in range(len(l)-2):
        key_pair = (l[i])+" "+(l[i+1])
        val = (l[i+2])
        if key_pair in d:
            d.setdefault(key_pair, []).append(val)
        else:
            d[key_pair] = [val]
    return d

def random_book():
    """
    This function randomly choosen starting point in the dictionary and then uses a loop to create a new list
    :return: a list
    """
    dic = dict_seed()
    start = random.choice(list(dic.keys()))
    temp = start.split()
    lst.extend(temp)
    lst.append(dic[start][random.randint(0,len(dic[start])-1)])
    for i in range(1, len(dic)-1):
        try:
            r = ' '.join(lst[i:])
            lst.append(dic[r][random.randint(0,len(dic[r])-1)])
        except KeyError:
            break
    return (lst)

def prnt_ran_bk():
    """
    This function prints the contents of the list
    :return: Prints the list
    """
    for i in random_book():
        print (i, end=" ")

print(prnt_ran_bk())