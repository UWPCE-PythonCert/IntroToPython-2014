'''
Created on Oct 30, 2014

@author: db345c
'''

import copy

def formatter():
    """ Use string fromatting with dictionary """
    food_prefs = {"name": u"Chris",
                  "city": u"Seattle",
                  "cake": u"chocolate",
                  "fruit": u"mango",
                  "salad": u"greek",
                  "pasta": u"lasagna"}
    
    print "{name} is from {city}, and he likes {cake}, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**food_prefs)

def createHex1():
    """ Populate set with integer and hex equivalent using loop """
    s = {}
    for i in range(16):
        s[i] = hex(i)
    print ", ".join(str(j) + "-" + str(s[j]) for j in s)

def createHex2():
    """ Populate set using dictionary comprehension """
    s = {i: hex(i) for i in range(16)}
    print ", ".join(str(j) + "-" + str(s[j]) for j in s)

def numberOfA():
    """ Count the number of 'a' in the dictionary values """
    food_prefs = {"name": u"Chris",
                  "city": u"Seattle",
                  "cake": u"chocolate",
                  "fruit": u"mango",
                  "salad": u"greek",
                  "pasta": u"lasagna"}
    my_prefs = copy.deepcopy(food_prefs)
    my_prefs = {i: my_prefs[i].count('a') for i in my_prefs }
    print my_prefs

def sets():
    """ Create three sets with numbers divisible by 2, 3, and 4 """
    s2 = (i for i in range(1, 21) if i % 2 == 0)
    print "\tMod (%) 2 -> " + ", ".join(str(j) for j in s2)
    s3 = (i for i in range(1, 21) if i % 3 == 0)
    print "\tMod (%) 3 -> " + ", ".join(str(j) for j in s3)
    s4 = (i for i in range(1, 21) if i % 4 == 0)
    print "\tMod (%) 3 -> " + ", ".join(str(j) for j in s4)
    
if __name__ == "__main__":
    print "Formatting String:", 
    formatter()
    print
    print "With Loop:", 
    createHex1()
    print
    print "List comprehension:", 
    createHex2()
    print
    print "Number of A's:",
    numberOfA()
    print
    print "Printing sets:"
    sets()