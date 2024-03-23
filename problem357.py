from typing import List
import math

def sieve(n: int) -> List[bool]:
 
    primes = [True] * (n+2)
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(2*i, len(primes), i):
                primes[j] = False
    return primes


def primeGenInts(n : int =10**9 ) -> int:
    resultSum = 0
    primes = sieve(n)
    for n in range(1, len(primes)-1):
        if not primes[n+1]:
            continue
        if primes[n+1]:
            nDividedD = n
            isPrimeGenInt = True
            for d in range(1, n):
                if n % d == 0:
                    # we only check half of divisors
                    if nDividedD == d:
                        break
                    nDividedD = n // d
                    if not primes[ d + (n // d) ]:
                        isPrimeGenInt = False
                        break
            if isPrimeGenInt:
                resultSum += n 
    return resultSum

print (primeGenInts(10000000))


