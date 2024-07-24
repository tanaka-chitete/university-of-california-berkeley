def wears_jacket_with_if(temp, raining):
    """
    Determines whether Alfonso will wear a jacket

    temp – a numeric value depicting a temperature
    raining – a boolean value telling if it is raining    

    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False


def wears_jacket(temp, raining):
    """
    Determines whether Alfonso will wear a jacket

    temp – a numeric value depicting a temperature
    raining – a boolean value telling if it is raining    

    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining


def is_prime(n):
    """
    Determines whether a given number N is a prime number

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True
     
