#!/usr/bin/env python3




def fibonacci(n):
    """Function to return the nth value in the Fibonacci series.
    
    Args:
        n (int): Nth number in the sequence to return the value of.
        
    fib(n) = fib(n-2) + fib(n-1)
    """
    if n == 1:
        print(0)
        return 0
    elif n == 2:
        print(1)
        return 1
    else:
        f = 0
        s = 1
        for i in range(2, n):
            p = f + s
            s = p
            f = p - f
            if i == n-1:
                print(p)
                return p
        
    

def lucas(n):
    """Function to return the nth value in the Lucas series.
    
    Args:
        n (int): Nth number in the sequence to return the value of.
        
    luc(n) = luc(n-2) + luc(n-1)
    """   
    if n == 1:
        print(2)
        return 2
    elif n == 2:
        print(1)
        return 1
    else:
        f = 2
        s = 1
        for i in range(2, n):
            p = f + s
            s = p
            f = p - f
            if i == n-1:
                print(p)
                return p
    
    
    
def sum_series(n, f=0, s=1):
    """Function to return the nth value in a sum series.
    
    Args:
        n (int): Nth number in the sequence to return the value of.
        f (int): First number in the sequence. Default is 0.
        s (int): Second number in the sequence. Default is 1.
    
    sum(n) = sum(n-2) + sum(n-1)   
    """   
    if n == 1:
        print(f)
        return f
    elif n == 2:
        print(s)
        return s
    else:
        for i in range(2, n):
            p = f + s
            s = p
            f = p - f
            if i == n-1:
                print(p)
                return p




if __name__ == "__main__":
    # run some tests
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8
    assert fibonacci(8) == 13
    
    assert lucas(1) == 2
    assert lucas(2) == 1
    
    assert lucas(5) == 7
    
    assert sum_series(5) == fibonacci(5)
    
    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)
    
    print("tests passed")


