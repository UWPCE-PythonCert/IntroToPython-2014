
def intsum():
    i = 0
    my_sum = 0
    while True:
        yield my_sum
        i += 1
        my_sum += i

def intsum2():
    i = 0
    my_sum = 0
    while True:
        yield my_sum
        i += 1
        my_sum += i

def doubler():
    i = 1
    while True:
        yield i        
        i *= 2

def fib():
    i = 0
    j = 1
    fib_n = 1
    while True:
        yield fib_n
        fib_n = i + j
        i = j
        j = fib_n

def prime():
    i = 1
    while True:
        print('i', i)
        i += 1
        for j in range(2,i):
            if not i % j:
                break
        else:
            yield i
