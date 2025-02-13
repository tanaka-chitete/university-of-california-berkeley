def trace1(fn):
    """Returns a version of fn that first prints before it is called.

    fn - a function of one argument
    """
    def traced(x):
        print("Calling", fn, "on argument", x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x**2

@trace1
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total
