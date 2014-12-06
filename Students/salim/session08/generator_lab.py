#!usr/local/bin/python


def intsum():
    args = [0, 1, 2, 3, 4, 5, 6, 7]
    x = 0
    for i in args:
        yield x + i
        x = x + i


def doubler():
    args = range(1, 100)
    x = 0
    for i in args:
        yield max([x * 2, 1])
        x = max([x * 2, 1])


def fib():
    l = [0, 0]
    while True:
        if sum(l) == 0:
            yield 1
            l.append(1)
        else:
            yield sum(l)
            l.append(sum(l))
        del l[0]


def prime():
    num = 1
    while True:
        num += 1
        prime = True
        for i in xrange(2, num + 1):
            if num % i == 0 and i != num:
                prime = False
                break
        if prime:
            yield num
