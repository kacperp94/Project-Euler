# https://projecteuler.net/problem=13

def n_digits_large_sum(block, n):
    large_sum = 0
    for l in range(1,101):
        large_sum+= int(block[n*(l-1):n*l])
    return str(large_sum)[:10]
