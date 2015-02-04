# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def multi_3_5(x):
    sum = 0
    for i in range((x-1)//3 + 1):
        sum += 3 * i
    for i in range((x-1)//5 + 1):
        sum += 5 * i
    for i in range((x-1)//15 +1):
        sum -= 15 * i
    return sum
def sum_int(x):
    output = 0
    for i in range(x):
        output += i
    return output
