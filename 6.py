# https://projecteuler.net/problem=6
def sum_sq_diff(x):
    sum_x_sq = 0
    sum_x = 0
    for i in range(x+1):
        sum_x_sq += i ** 2
    for i in range(x+1):
        sum_x += i
    
    return sum_x**2 - sum_x_sq
