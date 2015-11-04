#! /usr/bin/env python3


import random, re


txt = open('sherlock.txt')

words = txt.read().split()


def kata14(words):
    i = 1
    size = len(words)
    keys = {}
    while i < size:
        for word in words:
            keys.update({word: words[i:i+2]})
            i = i+1
    res = ''
    for k, v in keys.items():
        try:
            res += ' '.join((k, v[random.randrange(0, 1)]))
        except:
            try:
                res += ' '.join((k, v[0]))
            except:
                pass
        res += ' '
    res = re.sub(' and \Z', '.', res)
    res = res.replace("'", '')
    res = res.replace('"', '')
    res = res.replace('. ', '.  ')
    res = res.replace('? ', '?  ')
    res = res.replace('! ', '!  ')
    print(res)


if __name__ == '__main__':
    kata14(words)

