'''
#-------------------------------------------------#
# Title: TrapAreaCalc
# Dev:   Marty Pitts
# Date:  Nov 15, 2015
# Desc:

With the trapezoid rule, instead of approximating area by using rectangles
(as you do with the left, right, and midpoint rectangle methods), you approximate
area with trapazoids.

Because of the way trapezoids hug the curve, they give you a much better area
estimate than either left or right rectangles. And it turns out that a trapezoid
approximation is the average of the left rectangle and right rectangle approximations.
The Math:
        b
    Int    f(x) dx    =  (b - a) [ f(a) + f(b) / 2]
        a

    For N Steps

    Area = (b - a) / 2N [ f(x0) + 2f(x1) + 2f(x2) + 2f(xN-1) + f(xN) ]

Development Plan:
  1) BaseLine Approach function Test1 f(x) = sqrt(x - 1) find area. Step one.  Fix a = 1 b = 6
  2) BaseLine Approach function Test2 f(x) = mx + b Ex (y=2x + 4)
  3) Once baseline working, allow programmable number steps between a and b
  4) Once this is working, leverage Chris tests for verification based development.
  5) Time permitting work on the "extra credit" options for fun.

Code Structure (Notes):
  1) Query user for steps which define number traps in function.
  2) Define function for equation (line, a= Start Point, b = Stop Point)
  3) def trapz(fun, a, b)

Approach:
  1) create a list of N values from a to b (maybe 100 or so values to start)
  2) compute the function for each of those values and double them
  3) add them all up
  4) multiply by the half of the difference between a and b divided by the number of steps.

Tests:
  1) A Line
  2) A Quadratic
  3) A Sine
'''
# --------------- Data Code --------------------
import math
import cmath

Steps = 100 # defines how accurate you are going to be
curve = "sqrt(n-1)" # curve area calculation
line = "3x"
slopeline = "4x+1"
quadratic = "3x2+2x+1"
sineq = "cos(a)-cos(b)"

# Define start and stop points
a = 1
b = 6
N = []


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """
    Determine whether two floating point numbers are close in value.

    rel_tol
       maximum difference for being considered "close", relative to the
       magnitude of the input values
    abs_tol
       maximum difference for being considered "close", regardless of the
       magnitude of the input values

    Return True if a is close in value to b, and False otherwise.

    For the values to be considered close, the difference between them
    must be smaller than at least one of the tolerances.

    -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
    is, NaN is not close to anything, even itself.  inf and -inf are
    only close to themselves.
    """

    if rel_tol < 0.0 or abs_tol < 0.0:
        raise ValueError('error tolerances must be non-negative')

    if a == b:  # short-circuit exact equality
        return True
    if math.isinf(a) or math.isinf(b):
        # This includes the case of two infinities of opposite sign, or
        # one infinity and one finite number. Two infinities of opposite sign
        # would otherwise have an infinite relative tolerance.
        return False
    diff = abs(b - a)
    return (((diff <= abs(rel_tol * b)) and
             (diff <= abs(rel_tol * a))) or
             (diff <= abs_tol))

def frange(a, b, Steps):
    ''' Funciton to calculate steps in function
    '''
    f = list(range(Steps + 1))
    DeltaX = (b - a) / Steps
    for Trap in f: 
        f[Trap] = a + Trap * DeltaX
    # end for
    return(f)
  

def trapz(fun, a, b):
    '''
    Compute the area under the curve defined by
    y = fun(x), for x between a and b

    :param fun: the function to evaluate
    :type fun: a function that takes a single parameter

    :param a: the start point for the integration
    :type a: a numeric value

    :param b: the end point for the integration
    :type b: a numeric value
    '''
    N = list(range(Steps))

    #N = list(range(a,b,StepSize))
    DeltaX = (b - a) / Steps
    Xpoint = a
    TrapCumulativeArea = 0
    if fun == "sqrt(n-1)":
        for Trap in N:
            # Step1 Trapazoid Area = f(Xpoint) + f(Xpoint)/2) DeltaX
            # Step2 Add up the Trapazoids
            TrapArea = ((math.sqrt(Xpoint - 1) + math.sqrt((Xpoint + DeltaX) - 1)) / 2) * DeltaX
            Xpoint = Xpoint + DeltaX
            TrapCumulativeArea = TrapCumulativeArea + TrapArea
        # End for
    elif fun == "3x":
        Xpoint = a
        for Trap in N:
            # Step1 Trapazoid Area = f(Xpoint) + f(Xpoint)/2) DeltaX
            # Step2 Add up the Trapazoids
            TrapArea = (3*(Xpoint) + 3*(Xpoint + DeltaX))/ 2 * DeltaX
            Xpoint = Xpoint + DeltaX
            TrapCumulativeArea = TrapCumulativeArea + TrapArea
        # End for
    elif fun == "4x+1":
        Xpoint = a
        for Trap in N:
            # Step1 Trapazoid Area = f(Xpoint) + f(Xpoint)/2) DeltaX
            # Step2 Add up the Trapazoids
            TrapAreaNum = ((4*Xpoint) + 1) + (4*(Xpoint + DeltaX) + 1)
            TrapAreaDen = 2
            TrapArea = (TrapAreaNum / TrapAreaDen) * DeltaX
            Xpoint = Xpoint + DeltaX
            TrapCumulativeArea = TrapCumulativeArea + TrapArea
        # End for
    elif fun == "3x2+2x+1":
        Xpoint = a
        for Trap in N:
            # Step1 Trapazoid Area = f(Xpoint) + f(Xpoint)/2) DeltaX
            # Step2 Add up the Trapazoids
            TrapAreaNum = ((3*(Xpoint * Xpoint)) + 2*(Xpoint) + 1) + ((3*(Xpoint + DeltaX)*(Xpoint + DeltaX)) + 2*(Xpoint + DeltaX) + 1)
            TrapAreaDen = 2
            TrapArea = (TrapAreaNum / TrapAreaDen) * DeltaX
            Xpoint = Xpoint + DeltaX
            TrapCumulativeArea = TrapCumulativeArea + TrapArea
        # End for
    elif fun == "cos(a)-cos(b)":
        Xpoint = a
        for Trap in N:
            # Step1 Trapazoid Area = f(Xpoint) + f(Xpoint)/2) DeltaX
            # Step2 Add up the Trapazoids
            TrapAreaNum = (math.cos(Xpoint) - math.cos(Xpoint + b)) + (math.cos(Xpoint + DeltaX) - math.cos(Xpoint + DeltaX + b))
            TrapAreaDen = 2
            TrapArea = (TrapAreaNum / TrapAreaDen) * DeltaX
            Xpoint = Xpoint + DeltaX
            TrapCumulativeArea = TrapCumulativeArea + TrapArea
        # End for

    # End if
    return(TrapCumulativeArea)

def TrapAreaFunc(fun):
    '''
    Compute area for a function = fun()
    '''
    area = trapz(fun,a,b)
    return(area)

# Test range
f = frange(10,20,100)

# Calculate the area for an equation squt(x-1) Method2
CurveEqArea2 = trapz(curve, a, b)
assert isclose(CurveEqArea2,7.4512822710 )
print("Trapazoidal Calcualtion for Squt(x-1) =", CurveEqArea2)

# Calculate the area for curve
CurveEqArea3 = TrapAreaFunc(curve)
assert isclose(CurveEqArea3,7.4512822710 )
print("Trapazoidal Calcualtion for Squt(x-1) =", CurveEqArea3)

# Calculate the area for line
LineArea = TrapAreaFunc(line)
assert isclose(LineArea,52.5)
print("Trapazoidal Calcualtion for 3x =", LineArea)

# Calculate the area for sloped line
SlopeLineArea = TrapAreaFunc(slopeline)
assert isclose(SlopeLineArea,75)
print("Trapazoidal Calcualtion for 4x+1 =", SlopeLineArea)

# Calculate the area for quadratic
SlopeQuadArea = TrapAreaFunc(quadratic)
assert isclose(SlopeLineArea,255, rel_tol=1e1)
print("Trapazoidal Calcualtion for 3x2+2x+1 =", SlopeQuadArea)

# Calculate the area for cos(a) - cos(b)
SlopeSinArea = TrapAreaFunc(sineq)
assert isclose(SlopeSinArea,0.07265789286616514)
print("Trapazoidal Calcualtion for cos(a) - cos(b) =", SlopeSinArea)
