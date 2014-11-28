def string_splosion(str):
    newstr = str
    newstr2 = str
    strlength = len(str)
    for i in range(1,strlength+1):
        newstr1 = newstr[:(strlength - i)]
        newstr2 = newstr1+ newstr2
    return(newstr2)

