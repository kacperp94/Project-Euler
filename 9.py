# https://projecteuler.net/problem=9
def pyth_triplet(x):
    for a in range(1,x):
        for b in range(1,x-1):
            c = x - b - a
            if a ** 2 + b ** 2 == c ** 2:
                print(a, b, c)
                return a * b * c
    return 0

