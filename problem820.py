from math import floor

def nthDigitReciprocal(divisor: int, nthDigit: int)-> int:
    return (floor(10 * (10**(nthDigit-1) % divisor) / divisor)) % 10

def sumNthDigitReciprocals(nthDigit: int)-> int:
    resultSum = 0
    for divisor in range(1, nthDigit+1, 1):
        resultSum += nthDigitReciprocal(divisor, nthDigit)
    return resultSum

print(sumNthDigitReciprocals(100))



