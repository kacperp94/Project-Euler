# https://projecteuler.net/problem=25
def fib1(n):
    a,b = 0, 1
    numbers = []
    while b < n:
        a, b = b, a + b
        numbers.append(b)
        if b > n:
            l = numbers.index(b)
    return l
