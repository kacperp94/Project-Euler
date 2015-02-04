# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
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
