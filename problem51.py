import math
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

def hasThreeRepeatingDigits(prime : int) -> bool:
    digit_count = {} 
    for digit in str(prime):
        digit_count[digit] = digit_count.get(digit, 0) + 1
        if digit_count[digit] == 3:
            return True
    for count in digit_count.values():
        if count >= 3:
            return True
    return False

def findRepeatingDigit(prime: int) -> int:
    digit_count = {}
    for digit in str(prime):
        digit_count[digit] = digit_count.get(digit, 0) + 1
    for digit, count in digit_count.items():
        if count == 3:
            return int(digit)
    return -1


def hasEightFamily(primesWithThreeRepeatingDigits: List, prime: int, repeatingDigit :int)-> bool:
    count = 0
    for i in range(0, 10):
        primeFamMember = int(str(prime).replace(str(repeatingDigit), str(i)))
        if primeFamMember in primesWithThreeRepeatingDigits:
            count += 1
    if count == 8:
        return True
    return False

def smallestEightPrimeValueFamily(primesWithThreeRepeatingDigits : List[int]) -> int:
    for prime in primesWithThreeRepeatingDigits:
        repeatingDigit = findRepeatingDigit(prime)
        if hasEightFamily(primesWithThreeRepeatingDigits, prime, repeatingDigit):
            return prime
    return -1

# modular arithmetic reveals that we must at least replace 3 primes
def findSmallestPrimeOfEightPrimeValueFamily(n: int = 10**6) -> int:
    primes = sieve(n)
    primesWithThreeRepeatingDigits = []
    for i in range(len(primes)):
        if hasThreeRepeatingDigits(primes[i]):
            primesWithThreeRepeatingDigits.append(primes[i])

    smallest = smallestEightPrimeValueFamily(primesWithThreeRepeatingDigits)
    
    return smallest

print(findSmallestPrimeOfEightPrimeValueFamily())