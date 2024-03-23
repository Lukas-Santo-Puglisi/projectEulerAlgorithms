from typing import List


def sieve(n : int) -> List[int]:
    sieve = [True]* (n+1)
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(2*i, len(sieve) , i):
                sieve[j] = False
    
    return primes

#to understand this, study Wilsons theorem and compute by hand (p-1)*...*(p-4) mod p
def computePrimeFactorial(prime: int)-> int:
   
   return (-3*pow(8, prime-2, prime)) % prime

def sumPrimeFactorial(nonInclusiveLimit: int = 10**6)->int:
    resultSum = 0

    primes = sieve(nonInclusiveLimit)
    for prime in primes:
        resultSum += computePrimeFactorial(prime)
    return resultSum

print (sumPrimeFactorial())