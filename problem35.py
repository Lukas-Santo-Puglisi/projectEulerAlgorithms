from typing import List, Set
from math import sqrt

def getPrimes(limit:int)-> List[int]:
    sieve = [True]*(limit+1)
    sieve[0] = sieve[1] = False
    for cand_prime in range(2, int(sqrt(len(sieve))) + 1):
        if sieve[cand_prime]:
            for notPrime in range(cand_prime*cand_prime, len(sieve)-1, cand_prime):
                sieve[notPrime] = False
    return [cand_prime for cand_prime in range(len(sieve)) if sieve[cand_prime]]

#avoiding string manipulation
def isCircularPrime(prime: int, primesSet: Set[int])-> bool:
    num_digits = len(str(prime))
    multiplier = 10 ** (num_digits - 1)
    rotated = prime
    for _ in range(num_digits):
        if rotated not in primesSet:
            return False
        rotated = (rotated % 10) * multiplier + (rotated // 10)
    return True

def findAllCircularPrimes(limit: int = 10**9)-> List[int]:
    primeList = getPrimes(limit)
    circularPrimes = []
    primeSet = set(primeList)
    for prime in primeList:
        if isCircularPrime(prime, primeSet):
            circularPrimes.append(prime)
    return circularPrimes

print(len(findAllCircularPrimes()))




            