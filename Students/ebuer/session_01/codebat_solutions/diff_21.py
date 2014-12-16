def diff21(n):
    if n >= 21:
        return 2 * (n - 21)
    else:
        return 21 - n

n = 21
ans = diff21(n)

print ans
