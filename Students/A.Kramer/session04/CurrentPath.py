'''
Created on Oct 23, 2014

@author: db345c
'''
import os

def printCurrentDirectory(dir1=os.getcwd()):
    """ Print the content of the directory """
    lst = os.listdir(dir1)
    print dir1
    for f in lst:
        print os.path.join(dir1, f)

if __name__ == "__main__":
    """ Print the content of the directory """
    printCurrentDirectory()
    