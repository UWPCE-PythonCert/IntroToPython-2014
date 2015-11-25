#! /usr/bin/env python 3


def lambda_keyword(n):
    l = []
    for i in range(n):
        l.append(lambda x: i+1)
    print(l)

if __name__ == '__main__':
    lambda_keyword(4)
