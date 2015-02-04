def largest_pf(x):
    primes = []
    z=x
    for i in range(x//2+1,2, -1):
        if z % i == 0:
            for l in range(3, i//2):
                if i % l != 0:
                    primes.append(i)
                    z = z/i
    return primes
