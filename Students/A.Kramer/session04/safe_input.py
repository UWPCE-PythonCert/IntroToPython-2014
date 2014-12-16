'''
Created on Oct 22, 2014

@author: db345c
'''

def safe_input():
    try:
        s = raw_input("Enter something: ")
    except EOFError, KeyboardInterupt:
        return None
    return s

if __name__ == "__main__":
    print safe_input()