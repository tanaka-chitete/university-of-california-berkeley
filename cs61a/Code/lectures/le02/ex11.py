def knap(n, k):
    if n == 0:
        return k == 0
    else:
        with_last = knap(n // 10, k - n % 10)
        without_last = knap(n // 10, k)
        return with_last or without_last
