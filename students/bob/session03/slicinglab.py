# week 3 lab

lest = [0:21]

def flip(lest):
    return(lest[-1]+lest[1:-2]+lest[0])

def skip(lest):
    return(lest[::2])

def d4(lest):
    return(lest[4:-5:2])

def reverse(lest):
    return(lest[::-1])

def switch3rd(lest):
    third = len(lest)/3
    return(lest[third*2:third*3]+lest[third*0:third*1]+lest[thrid*1:third*2])