'''warmup: some algorithms related to numbers
'''

def factorial(n: int):
    '''n!
    '''
    import functools
    import operator

    return functools.reduce(operator.mul, range(1, n+1), 1)


def permutation(n: int, k: int):
    '''P(n, k) = n!/(n-k)!
    
    >>> permutation(10, 0)
    1
    >>> permutation(10, 2)
    90
    >>> permutation(10, 10)
    3628800
    >>> permutation(1000, 2)
    999000
    '''
    return factorial(n) // factorial(n - k)


def combination(n: int, k: int):
    '''C(n, k) = P(n, k)/k! = n!/((n-k)! * k!)
    
    >>> combination(10, 0)
    1
    >>> combination(10, 2)
    45
    >>> combination(10, 10)
    1
    >>> combination(1000, 2)
    499500
    >>> combination(1000, 998)
    499500
    '''
    return permutation(n, k) // factorial(k)


if __name__ == '__main__':
    import doctest
    doctest.testmod()