"""
Reads the kata_dfile (kata dictionary) and makes a kata from a seed
"""

import ast, csv

katadict = dict()

with open('kata_dfile3.txt', 'r') as f:
    values = f.readline()
    values = values.split(',')

    for v in values:
        temp = v.split(': ')
        katadict.setdefault(eval(temp[0]), eval(temp[1]))





# katadict = dict(temp)

