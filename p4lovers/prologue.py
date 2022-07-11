def factorial(n: int):
    '''n!
    '''
    import functools
    import operator

    return functools.reduce(operator.mul, range(1, n+1), 1)


def permutation(n: int, k: int):
    '''P(n, k) = n!/(n-k)!
    '''
    return factorial(n) // factorial(n - k)

def test_permutation():
    assert permutation(10, 0) == 1
    assert permutation(10, 2) == 90
    assert permutation(10, 10) == 3628800
    assert permutation(1000, 2) == 999000


def combination(n: int, k: int):
    '''C(n, k) = P(n, k)/k! = n!/((n-k)! * k!)
    '''
    return permutation(n, k) // factorial(k)

def test_combination():
    assert combination(10, 0) == 1
    assert combination(10, 2) == 45
    assert combination(10, 10) == 1
    assert combination(1000, 2) == 499500
    assert combination(1000, 998) == 499500
