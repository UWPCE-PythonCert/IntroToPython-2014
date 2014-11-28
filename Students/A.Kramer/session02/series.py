
def fibonacci(n):
    """Return Fibonacci number"""
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Return Lucas number"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

def sum_series(n, x=0, y=1):
    """Return either fibonacci or lucas numbers"""
    if x == 0 and y == 1:
        return fibonacci(n)
    elif x == 2 and y == 1:
        return lucas(n)
    else:
        return "Other Series"

if __name__ == '__main__':
    """Test internal assertions about function calls"""
    assert fibonacci(6) == 8
    assert fibonacci(3) == 2
    assert fibonacci(30) == 832040

    assert lucas(3) == 4
    assert lucas(5) == 11
    assert lucas(8) == 47 
    assert lucas(12) == 322
    
    assert sum_series(3) == 2
    assert sum_series(6) == 8
    
    assert sum_series(3, 2, 1) == 4
    assert sum_series(5, 2, 1) == 11
    assert sum_series(8, 2, 1) == 47