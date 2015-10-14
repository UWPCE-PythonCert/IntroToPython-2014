def dumb_grid():
    print( '''
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - + ''')

def _is_odd(n):
    return not n % 2 == 0

def _vertical(n):
    n = n if _is_odd(n) else n + 1
    return '|' + ' ' * ((n-3)//2) + '|' + ' ' * ((n-3)//2) + '|'
    
def _horizontal(n):
    n = n if _is_odd(n) else n + 1
    return '+' + '-' * ((n-3)//2) + '+' + '-' * ((n-3)//2) + '+'

def square_grid(n):
    # n must be an int
    n = int(n)

    # n must be at least 3
    if n < 3:
        n = 3

    print(_horizontal(n))
    for i in range((n-3)//2):
        print(_vertical(n))
    print(_horizontal(n))
    for i in range((n-3)//2):
        print(_vertical(n))
    print(_horizontal(n))

