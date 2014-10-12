def string_bits(str):
    strlength = len(str)
    newstr = ''
    for i in range(1,strlength+1,2):
      newstr = newstr + str[(i-1):i]
    return(newstr)
