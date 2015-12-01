def counter():
    print('counter: starting counter')
    i = -3
    while i < 3:
        i = i + 1
        print('counter: yield', i)
        yield i
    return None


# if __name__ == '__main__':
#     print "the generator function:"
#     print repr(counter)
#     print "call generator function"

#     c = counter()
#     print "the generator:"
#     print repr(c)

#     print 'iterate'
#     for item in c:
#         print 'received:', item
