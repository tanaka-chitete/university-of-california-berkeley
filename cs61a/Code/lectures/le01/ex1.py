def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def search_modified(f):
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    return x == 3


def square(x):
    return x**2


def positive(x):
    return max(0, square(x) - 100)


def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x: f(x) == y)
