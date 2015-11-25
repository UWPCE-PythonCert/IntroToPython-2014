#--data--


#--processing--
def line (x):
    '''a very simple straight horizontal line at y = 5'''
    return x

def trapz(fun, a, b, *args, **kwargs):
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
    # print(args)
    # print(kwargs)
    xlist = frange(a, b, 100)
    ylist=[]
    for x in xlist [1:-1]:
        ylist.append(fun(x,*args,**kwargs))
    area = (sum(ylist) + ((fun(a, *args,**kwargs) +fun(b, *args,**kwargs))/2))*((b-a)/100)
    return area

def frange (a, b, N):
    dx = (b-a)/N
    l =[]
    for i in range(N):
        l.append(a+(i*dx))
    l.append(b)
    return l

def quadratic (x, A, B, C):
    '''a very simple straight horizontal line at y = 5'''
    return A*(x**2) + B*x + C





















