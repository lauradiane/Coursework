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