def last2(str):
    str1 = str[-2:]
    n = len(str) 
    count1 = 0
    for i in range(n-1):
        # only check substring with length 2 from far left to two to far right in the string. 
        if i+2 <= n-1: 
            if str[i:(i+2)] == str1:
                count1 = count1 + 1
    return(count1)
