def trapz(fun, a, b):
    """
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for teh integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    """
    

    #compute the range 
    n =  100
    vals = frange(
    s = sum([fun(x, *args, **kwargs) for x in vals[1:-1]])
    s += (fun(a, *args, **kwargs) + fun(b, *args, **kwargs))/2
    s *= (b-a) / n

    
    
