# https://projecteuler.net/problem=56

def listnum(x):
    list1 = []
    for i in range(5,x):
        for i1 in range(5,x):
            c = str(i ** i1)
            m = 0
            for i2 in range(len(c)):
                m += int(c[i2])
            list1.append(m)
    return max(list1)


