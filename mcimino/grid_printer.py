def print_top(n):
    print('+', '--' * n, '+', '--' * n, '+')

def print_middle(n):
    for x in range(0, n+1):
        print('|', '  ' * n, '|', '  ' * n, '|')
    

def print_grid(n):
    print_top(n)
    print_middle(n)
    print_top(n)
    print_middle(n)
    print_top(n)

print_grid(5)