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
    l = [0, 1]
    for i in range(1, 100):
        if i == 0:
            yield 1
        else:
            l.append(l[-1] + l[-2])
            yield l[-1]
