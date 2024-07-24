def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)  
    True
    """
    def update(func):
        nonlocal n
        n = func(n)
        return n 
    return update


def nonlocalist(): 
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    get = lambda x: "Index out of range!" 
    def prepend(value):
        _______________________________________________________
        f = ___________________________________________________ 
        def get(i):
            if i == 0: 
                return value
            return ___________________(_______________________) 
        _______________________________________________________ 
    return prepend, get


 
