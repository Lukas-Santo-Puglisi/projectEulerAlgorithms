import math

def getLargestPrimeFactor(n):
    largestPrimeFactor = 1
    for i in range(2, math.floor(math.sqrt(n))):
        while n % i == 0 and n> 1:
            largestPrimeFactor = i
            n = n // i
    if largestPrimeFactor == 1:
        largestPrimeFactor = n
    return largestPrimeFactor

result = getLargestPrimeFactor(600851475143)
print(result)

    