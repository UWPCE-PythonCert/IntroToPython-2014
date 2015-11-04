__author__ = 'Max'

def firstthreenums(numlist):
    s = "the first 3 numbers are: {0}, {1}, {2}"
    argStr = ', '.join(str(x) for x in numlist)
    print(argStr)
    s.format(argStr)
    print(s)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    firstthreenums(l)