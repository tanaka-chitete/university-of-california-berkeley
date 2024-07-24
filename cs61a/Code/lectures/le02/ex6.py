def split(n):
    """Split a positive integer into all but its last digit and its last digit

    >>> all_but_last, last = split(2013)
    >>> all_but_last
    201
    >>> last
    3
    """
    return n // 10, n % 10


def sum_digits(n):
    """Return the sum of the digits of positive integer n"""

    if n <= 9:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def sum_digits_iter(n):
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum


def luhn_sum(n):
    if n <= 9:
        return n
    else: 
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
