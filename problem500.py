from typing import List

# 7376507

def sieve(n : int) -> List[int]:
    sieve = [True]* (10**8)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(2*i, len(sieve) , i):
                sieve[j] = False
    
    return primes


def findSmallestNumbersWithALotOfDivisors()-> int:
    primes = sieve(n=8000000)
    print(f'Number of primes ${len(primes)}')
    print(f'Biggest prime ${primes[-1]}')

    primeContainer = []
    for prime in primes:
        if prime**1 < 7376507:
            primeContainer.append(prime**1)
        if prime**2 < 7376507:
            primeContainer.append(prime**2)
        if prime**4 < 7376507:
            primeContainer.append(prime**4)
        if prime**8 < 7376507:
            primeContainer.append(prime**8)
        if prime**16 < 7376507:
            primeContainer.append(prime**16)
        if prime**32 < 7376507:
            primeContainer.append(prime**32)

    print(f'length of prime container {len(primeContainer)}')
    sorted(primeContainer)
    result = 1
    for i in range(500500):
            result *= primeContainer[i]
    return  result % 500500507


print(findSmallestNumbersWithALotOfDivisors())