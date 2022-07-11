'''
Prologue: Ancient Greek Mathematics and the Foundations of Computational Thinking
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


def trivia_gcd(a: int, b: int) -> int:
    '''
    >>> trivia_gcd(378, 273)
    21
    '''
    gcd = 1
    m = min(a, b)
    for i in range(1, m+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


def euclid_gcd(a: int, b: int) -> int:
    '''
    >>> euclid_gcd(378, 273)
    21
    '''
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


if __name__ == '__main__':
    import doctest
    doctest.testmod()