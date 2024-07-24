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
    return True if (temp < 60 or raining) else False


def is_prime(n):
    """
    Determines whether a given number N is a prime number

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    prime = False
    if n == 0:
        return prime
    elif n == 1: 
        return prime

    prime, k = True, 2
    while k < n and prime:
        if n % k == 0:
            prime = False 
        else:
            k += 1
    return prime
     
