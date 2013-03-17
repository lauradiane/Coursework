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
