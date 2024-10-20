def is_odd(n: int) -> bool:
    '''
    Assert whether a given integer is odd.
    '''
    return bool(n % 2)


def is_even(n: int) -> bool:
    '''
    Assert whether a given integer is even.
    '''
    return not is_odd(n)
