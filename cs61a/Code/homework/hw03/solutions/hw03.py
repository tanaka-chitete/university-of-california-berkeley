HW_SOURCE_FILE=__file__


def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    def func_adder(g):
        return composer(lambda x: func(g(x)))
    return func, func_adder


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n in (1, 2, 3):
        return n
    return g(n - 1) + 2*g(n - 2) + 3*g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c
"""This is an example of how a function might be easier to write recursively
as opposed to iteratively. Since we have defined G in terms of older versions of 
itself, the solution tends very naturally towards recursion.

The iterative solution is trickier, since we can only track a finate amount of 
state at a given time. We need to pick our variables carefully so that we have 
just the information we need to calculate the next step. In a sense, this 
problem is very similar to the Fibonacci sequence, assuming we start at the 0th
Fibonacci number:

f(n) = n,                 , if n <= 2
f(n) = f(n - 1) + f(n - 2), if n > 2

As you may recall, the solution for Fibonacci carried two variables around which
signified the previous two values.

def fib_iter(n):
    prev, curr = 0, 1
    while n > 0:
        prev, curr = curr, prev + curr
    return prev

Since G depends on the three previous values, it might make sense that we might
have to track three values instead.

Consider the three previous values OLD, OLDER and OLDEST. To do an update, OLDER
ages and becomes OLDEST, OLD becomes OLDER and OLD gets the new value which is 
derived from the three previous values: old + 2*older + 3*oldest
"""

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n < 10:
        return 0
    last, rest = n % 10, n // 10
    return max(last - rest % 10 - 1, 0) + missing_digits(rest)
"""The equivalent iterative version of this problem might look something like 
this:

missing = 0
while n > 10:
    last, rest = n % 10, n // 10
    missing += max(last - rest % 10 - 1, 0)
    n //= 10
return missing

A tricky case for this problem was handling adjacent numbers that are the same -
that's why we wrap the digit difference each recursive call with a max 
comparison call to 0
"""


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    def constrained_count(total, smallest_coin):
        if total == 0:
            return 1
        if smallest_coin > total:
            return 0
        without_coin = constrained_count(total, smallest_coin * 2)
        with_coin = constrained_count(total - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_coin(total, 1)
"""This is remarkably similar to the COUNT_PARTITIONS problem, with a few minor
differences:

- A maximum partition size M is not given, so we need to create a helper
  function that takes in two arguments and also create another helper function
  to find the max coin.
- Partition size is not linear, but rather multiples of two. To get the next
  partition you need to divide by two instead of subtracting by one.

One other implementation detail here is that we enforce a maximum partition
size, rather than a minimum coin. Many students attempted to start at 1 and work
their way up. That will also work, but is less similar to count partitions. As
long as there is some ordering on the coins being enforced, we ensure we cover
all combinations of coins without any duplicates.
"""

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(start, end)
    else:
        middle = 6 - start - end
        move_stack(n - 1, start, middle)
        print_move(start, end)
        move_stack(n - 1, middle, end)
"""To solve the Towers of Hanoi problem for N disks we need to do three steps:

1. Move everything by the last disk (N - 1) sisks to someplace in the middle
   (not the start nor end rod).
2. Move the last disk (a single disk) to the end rod. This must occur after step
   1 (we have to move everything above it away first)!
3. Move everything but the last disk (the disks from step 1) from the middle to
   on top of the last rod.

We take advantage of the fact that MOVE_STACK is guaranteed to move N disks from
START to END while obeying the rules of Towers of Hanoi. The only thing that
remains is to make sure that we have set up the playing board to make that
possible.

Since we move a disk to the end rod, we run the risk of MOVE_STACK doing an 
improper move (big disk on top of small disk). But since we're moving the 
biggest disk possible, nothing in the N - 1 disks above that is bigger. 
Therefore, even though we do not explicitly state the Towers of Hanoi 
constraints, we can still carry out the correct steps.
"""


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'

