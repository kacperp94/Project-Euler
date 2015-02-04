# https://projecteuler.net/problem=48
def last_n_dig(x, n):
    sum_x = 0
    for i in range(1,x+1):
        sum_x += i ** i
    return str(sum_x)[-n:]
