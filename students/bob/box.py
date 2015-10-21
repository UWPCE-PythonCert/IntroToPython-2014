#!/usr/bin/python

n = input('integer? ')

def box(n):
    print('+ '+'- '*n+'+ '+'- '*n+'+')
    x=1
    while x <= n:
        print('| '+' '*n*2+'| '+' '*n*2+'|')
        x+=1
    print('+ '+'- '*n+'+ '+'- '*n+'+')
    x=1
    while x <= n:
        print('| '+' '*n*2+'| '+' '*n*2+'|')
        x+=1
    print('+ '+'- '*n+'+ '+'- '*n+'+')

box(n)
