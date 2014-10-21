'''
Created on Oct 1, 2014

@author: db345c
'''

def rot13(s):
    alpha1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .!<>;:'"
    alpha2 = "NOPQRSTUVWXYZabcdefgjijklmnopqrstuvwxyzABCDEFGHIJKLM .!<>;:'"
    
    # string to return
    ret = ""
    
    for i in range(0, len(s)):
        try:
            if s[i].islower():
                ret += alpha2[alpha1.index(s[i])].lower()
            else:
                ret += alpha2[alpha1.index(s[i])].upper()
        except ValueError:
            pass
        else:
            pass
    return ret

# run the program with the assigned parameter
if __name__ == '__main__':
    print rot13("Zntargvp sebz bhgfvqr arne pbeare")
    
    
