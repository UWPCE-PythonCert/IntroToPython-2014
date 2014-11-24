'''
Write a function that returns a list of n functions, such that each one, when called, will return the input value, incremented by an increasing number.

Use a for loop, lambda, and a keyword argument

( Extra credit ):

Do it with a list comprehension, instead of a for loop

Not clear? heres what you should get


In [96]: the_list = function_builder(4)
### so the_list should contain n functions (callables)
In [97]: the_list[0](2)
Out[97]: 2
## the zeroth element of the list is a function that add 0
## to the input, hence called with 2, returns 2
In [98]: the_list[1](2)
Out[98]: 3
## the 1st element of the list is a function that adds 1
## to the input value, thus called with 2, returns 3
In [100]: for f in the_list:
    print f(5)
   .....:
5
6
7
8
### If you loop through them all, and call them, each one adds one more
to the input, 5... i.e. the nth function in the list adds n to the input.

'''

def function_build(n):
    l = []
    for  i in range(n):
        l.append(lambda x,j=i:x+j)
    return l

if __name__ == "__main__":
    the_list = function_build(4)
    print the_list[0](2)
    print the_list[1](2)
    for f in the_list:
        print f(5)
        
    #And now in a list comprehension
    the_list = [lambda x,j=i:x*j for i in range(5)]
    print the_list[0](2)
    print the_list[1](2)
    for f in the_list:
        print f(5)   
        
   
   
        