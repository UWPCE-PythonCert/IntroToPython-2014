def print_grid(n, m):
    square = ''
    for x in range(1, n + 1):
        line = ''

        if (x == 1) or (x == n) or (x == int(n / 2)):
            for y in range(1, m + 1):
                if (y == 1) or (y == m) or (y == int(m / 2)):
                    line += 'x'
                else:
                    line += '-'
        else:
            for y in range(1, m + 1):
                if (y == 1) or (y == m) or (y == int(m / 2)):
                    line += '|'
                else:
                    line += ' '
        square += line + "\n"
    return square

print(print_grid(20, 40))
