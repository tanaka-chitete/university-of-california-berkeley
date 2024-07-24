def count_while(s, target):
    """Count the number of times that VALUE appears in sequence S.

    >>> count_while([1, 2, 3, 4, 4, 5, 4], 4)
    3
    """
    i, total = 0, 0
    while i < len(s):
        element = s[i]
        if element == target:
            total += 1
        i += 1
    return total


def count_for(s, target):
    """Count the number of times that VALUE appears in sequence S.

    >>> count_for([1, 2, 3, 4, 4, 5, 4], 4)
    3
    """
    total = 0
    for element in s:
        if element == target:
            total += 1
    return total
