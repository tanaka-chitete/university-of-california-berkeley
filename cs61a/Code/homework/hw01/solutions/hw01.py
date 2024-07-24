from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)
"""If b is positive, we add the numbers together. If b is negative, we
   subtract the numbers. Therefore, we choose the operator add or sub based
   on the sign of b.
"""


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return min(x**2 + y**2, x**2 + z**2, y**2 + z**2) # or x**2 + y**2 + z**2 - max(x, y, z)**2
"""We use the fact that if x > y and y > 0, then square(x) > square(y). So, we 
   can take the min of the sum of squares of all pairs. The min function can 
   take an arbitrary number of arguments.

   Alternatively, we can do the sum of all squares of all the numbers. Then, we 
   pick the largest value, and subtract the square of that.
"""


def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    found = False
    factor = x - 1
    while factor > 0 and not found:
        if x % factor == 0:
            found = True
        else:
            factor -= 1
    return factor
"""Iterating from x - 1 to 1, we return the first integer that evenly divides x. 
   This is guaranteed to be the largest factor of x.
"""


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())

def cond():
    return False

def true_func():
    print(42) 

def false_func():
    print(47)
"""The function with_if_function uses a call expression, which garuantees that 
   all of its operand subexpressions will be evaluated before if_function is 
   applied to the resulting arguments.

   Therefore, even if cond returns False, the function true_func will be called. 
   When we call true_func, we print out 42. Then, when we call false_func, we 
   will also print 47.

   By contrast, with_if_statement will never call true_func if cond returns
   False. Thus, we will only call false_func, printing 47.
"""

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    length = 1
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x // 2 # Integer division prevents output of "1.0"
        else:
            x = x * 3 + 1
        length = length + 1
    print(x) # x is now 1
    return length
"""We keep track of the current length and current value of the sequence. From
   there, we loop until we hit the end of the sequence, updating the length in
   each step.
"""
