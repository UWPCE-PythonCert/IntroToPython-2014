def print_grid(n):
    for x in range(1, n + 1):
        line = ''
        if (x == 1) or (x == n) or (x == int(n / 2)):
            for y in range(1, n + 1):
                if (y == 1) or (y == n) or (y == int(n / 2)):
                    line = line + 'x'
                else:
                    line += '-'
        else:
            for y in range(1, n + 1):
                if (y == 1) or (y == n) or (y == int(n / 2)):
                    line += '|'
                else:
                    line += ' '
        print(line)

print_grid(20)
