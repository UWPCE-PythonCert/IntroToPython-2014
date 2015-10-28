#! /usr/bin/env python3



# 'file_002 :   123.46, 1e+04'

t = ( 2, 123.4567, 10000)

print('file_00{} :{:9.5}, {:.1e}'.format(*t))
      



from random import randrange

r = randrange(3,20)
l = []
for i in range(1,r):
    l.append(randrange(1,100))
    
print(l)
print("the first 3 numbers are: {:d}, {:d}, {:d}".format(*l))