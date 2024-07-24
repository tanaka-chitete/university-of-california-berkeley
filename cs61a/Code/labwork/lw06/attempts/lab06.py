this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    inc = 0
    def adder_inc(b):
        nonlocal inc
        amount = a + b + inc 
        inc += 1 # For subsequent calls
        return amount
    return adder_inc


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    num_calls, fir, sec = 0, 0, 1
    def fib():
        nonlocal num_calls, fir, sec
        if num_calls == 0: # Base case - 0 is first Fibonacci number
            nxt = 0
        elif num_calls == 1: # Base case - 1 is second Fibonacci number
            nxt = 1
        else: 
            nxt = fir + sec
            fir, sec = sec, fir + sec 
        num_calls += 1
        return nxt
    return fib

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    if entry == elem: # Prevent infinite loop
        skip = True
    else:
        skip = False

    i = 0
    n = len(lst)
    while i < n:
        if lst[i] == entry:
            lst.insert(i + 1, elem)
            if skip: # Skip over identical ENTRY and ELEMENT
                i += 1 
        i += 1
    return lst
