#mailroom program to break the monotony

import random

def rd():
    return round(random.random() * 100,2)

#this may be a bad idea but we will see, a list of tuples for clients
client_list = [
        ('Askew', 'Anne'),\
        ('Bocher', 'Joan'),\
        ('Clarkson', 'Jeremy'),\
        ('Hamont', 'Matthew'),\
        ('May', 'James'),\
        ('Parris', 'George van')
                ]

donations = [
        (client_list[0], rd(), rd(), rd()),
        (client_list[1], rd(), rd()),
        (client_list[2], rd(), rd(), rd()),
        (client_list[3], rd(), rd(), rd(), rd()),
        (client_list[4], rd(), rd(), rd()),
        (client_list[5], rd(), rd(), rd())
                ]

for c in client_list:
    for d in donations:
        if d[0] == c:
            temp_dontation = d[1:]

    print "Hello {first} {last}, thanks for donating ${value}"\
        .format(last = c[0], first= c[1], value=temp_dontation[0])
