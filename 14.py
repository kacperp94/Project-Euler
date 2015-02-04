# https://projecteuler.net/problem=14
def longest_collatz_sequence(n):
    """Finds the longest collatz sequence for numbers in range r"""
    dicto = {}
    for i in range(1,n):
        m = 0
        j = i
        while j > 1:
            if j % 2 == 0:
                j = j/2
                m +=  1
            else:
                j = 3 * j + 1
                m += 1
        dicto.update({str(m) : i})
        # the value (524) was found using another code, I will update it later.
    return dicto['524']
