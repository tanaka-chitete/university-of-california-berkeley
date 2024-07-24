def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    k = 2
    def prime_helper(n, k):
        if n == 1:
            return False
        elif n % k == 0:
            return False 
        else:
            return prime_helper(n, k + 1) if (k + 1 < n) else True
    return prime_helper(n, k)      


def count_stair_ways(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """
    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    pass


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [x * (x - 1) for x in s if (x - 1) % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive 
    elements of S.

    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    124
    >>> max_product([])
    1
    """
    if not s[]
        return 1
    else:
        ...


def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968
    False
    """
    pass 
