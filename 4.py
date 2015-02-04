"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def palindromeproduct(x, y):
    list_palin = []
    for i in range(100, x+1):
        for l in range(100, y+1):
            z = ''
            m = str(i * l)
            for k in range(len(m)):
                z += m[-k - 1]
            if str(z) == m:
                list_palin.append(int(m))
    return max(list_palin)
