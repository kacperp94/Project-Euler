# https://projecteuler.net/problem=20
def sum_of_digits_factorial(x):
    i = 1
    l = 1
    s = 0
    while i <= x:
        l *= i
        i += 1
    y = 0
    for m in range(len(str(l))):
        s+=int(str(l)[m])
    return s
