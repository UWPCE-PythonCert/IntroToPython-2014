def fibonacci(n):
    """Return the the value of n fibonacci"""
    if n == 0:
        return 0

    elif n == 1:
        return 1

    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n-2)



def lucus(n):
    """Return the lucus value of n """
    if n == 0:
        return 2

    elif n == 1:
        return 1

    elif n > 1:
        return lucus(n - 1) + lucus(n - 2)


def sum_series(a,b=0,c=1):
    """Return fibonacci or lucus depending on optional parms"""
    if b == 2 and c == 1:
        return lucus(a)
    else:
        return fibonacci(a)


#test that fibonacci function is working as expected
assert fibonacci(7) == 13,"There is a miscalculation with the fibonacci calculation"

#test that the lucus function is working as expected
assert lucus(5) == 11,"There is a miscalculation with the lucus calcuation"

#test that sum_series is returning a lucus number when optional
#parameters are 2 and 1.
assert sum_series(0,2,1) == 2,"An expected lucus number is not being returned"
