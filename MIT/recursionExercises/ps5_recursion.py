# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#

import string

def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    reversed_string = ''
    if len(aStr) == 1:
        return aStr
    else:
        reversed_string += aStr[-1]
        return reversed_string + reverseString(aStr[:-1])
# NOTE: had to create an output variable and concatenate it to recursion result
        

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == '':
        return True
    if word == '':
        return False
    if x[-1] == word[-1]:
        return x_ian(x[:-1], word[:-1])
    else:
        return x_ian(x, word[:-1])
        
