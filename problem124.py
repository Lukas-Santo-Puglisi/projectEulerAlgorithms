from typing import List
from math import sqrt
from functools import reduce
def getUniquePrimeFactors(candidate: int) -> List[int]:
    d = 2
    n = candidate
    factors = []
    while d * d <= candidate:  
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d  
        d += 1
    if n > 1:  
        factors.append(n)
    return list(set(factors))

def getRad(x: int)->int:
    factors = getUniquePrimeFactors(x)
    rad = reduce(lambda x, y: x*y, factors, 1)
    return rad

def getLastRad(limit: int = 10**5)->int:
    sortedAfterRad =  [i+1 for i in range(limit) ]
    sortedAfterRad.sort(key=getRad)
    print(sortedAfterRad)
    return sortedAfterRad[10**4-1]

print(getLastRad())


