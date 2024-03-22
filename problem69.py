#Let phi(n) be the totient function. Find n <= 1,000,000: n/phi(n) is maximum


import math

def primesUpToN(n):
    global primes
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(2*i, len(primes), i):
                primes[j] = False
    return primes

#p_1 /p_1 -1 * ... * p_l / p_l - 1

def nDividedByTotientFunction(n):
    result = 1
    for index, prime in enumerate(primes[:n+1]):
        if prime and n % index == 0:
                result *= (index / (index - 1) )


    return result

def findMaxNDividedByTotientFunction(n=10001):
    primesUpToN(n)
    currentMaxValue = 3
    currentMaxNumber = 6
    for i in range(7, n, 1):
        temp = nDividedByTotientFunction(i)
        if temp > currentMaxValue:
            currentMaxValue = temp
            currentMaxNumber = i
    return currentMaxValue, currentMaxNumber

print(findMaxNDividedByTotientFunction())








