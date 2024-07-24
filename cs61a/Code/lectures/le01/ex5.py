def make_adder(n):
    def adder(k):
        return k + n
    return adder

def square(x):
    return x**2

def triple(x):
    return 3 * x

def compose1(f, g): # HOF that takes two different functions, both of 1 argument
    def h(x):
        return f(g(x))
    return h
