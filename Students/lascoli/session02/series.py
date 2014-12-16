
def fib(n):
    """Return results , input parameter values ranging from 0 + to the Fibonacci Function."""
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)

if __name__ == '__main__':


    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

    print "All Test Pass Task 2 Fibonacci Function"



def lucas(n):
    """Return results , input parameter values ranging from 2 + to the Lucas Function."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

if __name__ == '__main__':

    assert lucas( 0) == 0
    assert lucas( 1) == 1
    assert lucas( 2) == 1
    assert lucas( 3) == 2
    assert lucas( 4) == 3
    assert lucas( 5) == 5

    print "All Test Pass Task 2 Lucas Function"


def sum_series (n, x=0, y=1) :
        """Return results , 1 mandatory and 2 optional input parameter values ranging """
        if n == 0 :
            return x
        elif n == 1 :
            return y
        else:
            return sum_series (n-1,x,y) + sum_series(n-2,x,y)

if __name__ == '__main__':

    assert sum_series( 0, 0, 1) == 0
    assert sum_series( 1, 0, 1) == 1
    assert sum_series( 2, 0, 1) == 1
    assert sum_series( 4, 0, 1) == 3
    assert sum_series( 0, 2, 1) == 2
    assert sum_series( 3, 2, 1) == 4
    assert sum_series( 4, 2, 1) == 7
    assert sum_series( 5, 2, 1) == 11

    print "All Test Pass Task 2 sum_series"  
