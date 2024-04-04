from typing import List
from math import sqrt
from functools import reduce
def getPrimes(limit: int)->List[int]:

    candidatePrimes = [True] * (limit + 1)
    candidatePrimes[0] = candidatePrimes[1] = False
    for candidatePrime in range(2, int(sqrt(limit))+1,1):
        if candidatePrimes[candidatePrime]:
            for notPrime in range(candidatePrime*candidatePrime, len(candidatePrimes), candidatePrime):
                candidatePrimes[notPrime] = False
    return [prime for prime in range(len(candidatePrimes)) if candidatePrimes[prime]]

def totient(d:int, primes: List[int])-> int:
    factors = []
    for candidateFactor in primes:
        if candidateFactor > d:
            break
        if d % candidateFactor == 0:
            factors.append(float(candidateFactor))
    # x is the accumulated value, y update value
            
    countRelPrimeToN = int(reduce(lambda accumulated, update : float(accumulated) * (1- (1/update)) ,factors, float(d)))

    return countRelPrimeToN

def countFractions(limit: int= 10**3)->int:
    
    resultCount = 0
    primes = getPrimes(limit)
    for d in range(2, limit+1, 1):
        resultCount += totient(d, primes)
    return resultCount

print(countFractions())







