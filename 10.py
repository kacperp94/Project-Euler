""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million. """
def sum_of_primes(x):
    """
    The function finds the sum of the first x primes.
    >>>sum_of_primes(10)
    17
    """
    list1 = [2]
    i = 0
    for n in range(3, x+1, 2):
        for l in range(2, int(n ** 0.5 + 1)):
            if n % l == 0:
                break
        else:
            list1.append(n)
            i += 1
    return sum(list1)
