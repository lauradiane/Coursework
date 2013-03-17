# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    result = 0
    for e in poly:
        result += e * x**(poly.index(e))
    return float(result)


# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    deriv = []
    exp = 0
    if len(poly) == 1:
        deriv.append(0.0)
    while exp != len(poly):
        if exp != 0:
            result = float(poly[exp] * exp)
            deriv.append(result)
        exp += 1
    return deriv



# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    count = 0
    while evaluatePoly(poly, x_0) > epsilon or evaluatePoly(poly, x_0) < (-epsilon):
        x_0 -= (evaluatePoly(poly,x_0)/evaluatePoly((computeDeriv(poly)),x_0))
        count += 1
    return [x_0, count]                                               
        
                                                         
        
                                                
                                        











