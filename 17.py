"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

def number_let_count(n):
    # works only for n<1000
    sum_let = 0
    numbers = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
               ,20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'}
    for i in range(1,n+1):
        if i in numbers and i != 100:
            sum_let += len(numbers[i])
        else:
            if i in range(21,100):
                sum_let += len(numbers[(i//10) * 10]) + len(numbers[i % 10])
            elif i in range(100,1000):
                if i % 100 == 0:
                    sum_let += len(numbers[(i//100)]) + len(numbers[100])
                else:
                    sum_let += len(numbers[(i//100)]) + len(numbers[100]) + len('and')
                    if 10<i % 100<20:
                        sum_let += len(numbers[i%100])
                    else:
                        sum_let += len(numbers[((i % 100)//10) * 10]) + len(numbers[(i % 100) % 10]) 
    return sum_let   
