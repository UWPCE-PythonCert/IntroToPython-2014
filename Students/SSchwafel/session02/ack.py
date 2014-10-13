#!/usr/bin/python

print """This program performs Ackermann's Function, as defined by: 

A(m,n) =

    n+1 if m = 0

    A(m-1) if m > 0 and n = 0

    A(m-1, A(m, n-1)) if m > 0 and n > 0


    """

m = raw_input("Please provide a value for m: ")
n = raw_input("Please provide a value for n: ")

m = int(m)
n = int(n)

print "m = " + str(m)
print "n = " + str(n)

def is_negative(x):

    if x < 0:

        x = raw_input("Ackermann's function is not defined for values less than 0. Please enter a value that is greater than 0: ")

        x = int(x) 

        if x < 0:
    
            print "Please start over with a positive value for m"
            exit()
    

    print x 

is_negative(m)


def ackermann(x,y):

    #x = m 
    #y = n 
    while y > -1:

        if x == 0:
        
            return y+1

        elif x > 0 and y == 0:

            return ackermann(x - 1, 1)

        elif x > 0 and y > 0:
            
            return ackermann(x - 1 , ackermann(x, y - 1))
        
print ackermann(n,m)
