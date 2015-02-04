# problem 1
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
