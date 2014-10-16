def labtest(s):
    a1 = s[0]
    z1 = s[-1]
    s[0] = z1
    s[-1] = a1
    return(s)
