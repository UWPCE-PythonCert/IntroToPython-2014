'''
Created on Oct 17, 2014

@author: db345c
'''

def rot13(s):
    
    ret = ""
    
    for c in s:
        var = ord(c)
        if var >= ord("a") and var <= ord("z"):
            if var > ord("m"):
                var -= 13
            else:
                var += 13
        if var >= ord("A") and var <= ord("Z"):
            if var > ord("M"):
                var -= 13
            else:
                var += 13
                
        ret += chr(var)
        
    return ret

if __name__ == "__main__":
    print rot13(rot13("Aleksey Kramer"))