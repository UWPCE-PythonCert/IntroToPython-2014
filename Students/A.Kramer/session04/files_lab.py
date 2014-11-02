'''
Created on Oct 22, 2014

@author: db345c
'''
import string

def uniqueLanguages(filename):
    # Creating set variable
    s = set()
    
    # Opening the file
    try:
        f = open(filename, "r")
    except IOError:
        print "Unable to open the file " + filename
        try:
            f.close()
        except Exception:
            return
    
    # Populating the set
    for student in f:
        (name, lang) = student.split(":")
        lst = lang.split()
        for i, j in enumerate(lst):
            lst[i] = j.strip(string.punctuation)
            s.add(lst[i].lower())
            
    # Trying to close the file
    try:
        f.close()
    except IOError:
        try:
            f.close()
        except:
            return
    
    # cheap way of removing fixed header
    try:
        s.remove("languages")
    except  KeyError:
        print "languages is not in the set"
    
    # print unique languages
    for i in s:
        print i.capitalize()

    
if __name__ == "__main__":
    uniqueLanguages("students.txt")