## What is the 10 001st prime number?

def findprime(x):
    """ finds x-th prime number as long as x-th prime is smaller than x ** 2
    >>>findprime(2)
    3
    >>>findprime(25000)
    287117
    """
    i = 0
    while i <= x:
        for n in range(3, x ** 2, 2):
            for l in range(2, int(n ** 0.5 + 1)):
                if n % l == 0: break
            else:
                i += 1
            if i == x-1:
                return n
