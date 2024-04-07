from typing import List
from math import sqrt
def getProperDivisors(candidate: int)-> List[int]:
    properDivisors = []

    for divisor in range(1, int(sqrt(candidate))+1, 1):
         if candidate % divisor == 0:
                properDivisors.append(divisor)
                if divisor != candidate//divisor:
                    properDivisors.append(candidate//divisor)
    properDivisors.remove(candidate)
    return properDivisors

def getAbundantNumbers(nonInclusiveLimit: int = 28124)-> List[int]:
    abundantNumbers = []
    for candidate in range(1, nonInclusiveLimit, 1):           
            properDivisorsSum = sum(getProperDivisors(candidate))
            if properDivisorsSum > candidate:
                abundantNumbers.append(candidate)
    return abundantNumbers

def getSumNumbersSumOfAbundantNumbers(nonInclusiveLimit: int = 28124)->int:
    
    abundantNumbers = getAbundantNumbers(nonInclusiveLimit)
    sieve = [False]* nonInclusiveLimit
    for firstSummandIndex in range(len(abundantNumbers)):
        for secondSummandIndex in range(firstSummandIndex, len(abundantNumbers)):
            candidate = abundantNumbers[secondSummandIndex] + abundantNumbers[firstSummandIndex]
            if candidate < nonInclusiveLimit:
                sieve[candidate] = True
    resultSum = sum([idx for idx, boolVal in enumerate(sieve) if boolVal == False])

    return resultSum

print(getSumNumbersSumOfAbundantNumbers())
    


