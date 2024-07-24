from operator import add, mul, truediv

def divide_all(n, ds):
    try:
        return reduce_rec(truediv, ds, n)
    except ZeroDivisionError:
        return float("inf")


def reduce_iter(f, s, initial):
    """Combine elements of S using F starting from INITIAL.

    >>> reduce_iter(mul, [2, 4, 8], 1)
    64
    >>> reduce_iter(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial


def reduce_rec(f, s, initial):
    """Combine elements of S using F starting from INITIAL.

    >>> reduce_rec(mul, [2, 4, 8], 1)
    64
    >>> reduce_rec(add, [1, 2, 3, 4], 0)
    10
    """
    if s == []:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce_rec(f, rest, f(initial, first))
