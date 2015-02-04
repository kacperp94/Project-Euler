def sum_even_fibonacci(n):
    a, s, b = 0, 0, 1
    while b < n:
        a,b = b, a + b
        if b % 2 == 0:
            s+= b
    return s

def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
