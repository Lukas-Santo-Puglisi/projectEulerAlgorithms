from typing import List, Set
from math import sqrt
from time import time
def getPrimes(limit :int = 10**7 -1)-> List[int]:
    primes = []
    sieve = [True]*(limit + 1)
    sieve[0] = sieve[1] = False
    for candidate in range(2, int(sqrt(len(sieve)))+1, 1):
        if sieve[candidate]:
            for nonPrime in range(candidate*candidate, len(sieve), candidate):
                sieve[nonPrime] = False
    primes = [primeNumber for primeNumber in range(len(sieve)) if sieve[primeNumber]]
    return primes
                           
def slidingWindows(primes: List[int], primeSet: Set[int], startingPoint, startWindowSize = 22, limit = 10**7-1):
    resultPrime = count = -1
    candidate = sum(primes[startingPoint: startingPoint + startWindowSize+1])
    while True:
        if candidate > limit:
            break
        if candidate in primeSet:
            resultPrime = candidate
            count = startWindowSize
        startWindowSize += 1
        candidate += primes[startingPoint + startWindowSize]
    return resultPrime, count

def findConsecutivePrimeSum(limit: int = 10**7-1):
    primes = getPrimes(limit)
    primeSet = set(primes)
    resultPrime = resultCount = -1
    startingPoint = 0
    while True:
        sumPrime, count = slidingWindows(primes, primeSet, startingPoint, startWindowSize = 2, limit = limit)
        if sumPrime == -1:
            break
        else:
            startingPoint += 1
            if count > resultCount:
                resultCount = count
                resultPrime = sumPrime
    return resultPrime
start = time()
primesum =findConsecutivePrimeSum(10**6)
end = time()
print(f'found consecutive prime sum: {primesum}')
print(f'time needed: {end-start}')
            





