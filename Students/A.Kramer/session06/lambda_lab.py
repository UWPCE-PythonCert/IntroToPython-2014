'''
Created on Nov 5, 2014

@author: Aleksey Kramer
'''

def function_bulider(n):
    l = []
    for i in range(n):
        l.append(lambda x, e=i: x + e)
    return l

if __name__ == "__main__":
    the_list = function_bulider(4)
    for f in the_list:
        print f(5)