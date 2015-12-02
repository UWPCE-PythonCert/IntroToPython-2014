def print_grid(x, y=1):
    plus = "+ "
    minus = "- "
    side = "| "
    blank = "  "
    top = (plus + (minus * y))
    middle = (side + (blank * y))
    for j in range (y):
        print ((top * x) + plus)
        for i in range(y):
            print ((middle * x) + side)
    print ((top * x) + plus)