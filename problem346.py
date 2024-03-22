
from math import log, floor, sqrt

def findSumStrongRepunits(nonInclusiveLimit: int = 10**12)->int:
    resultSum = 1 #1 only accounted for
    for candidate in range(2, nonInclusiveLimit):
        #digit length base > 3 for all bases
        upperBaseLimit = floor( sqrt(candidate) )
        for base in range(2, upperBaseLimit +1):
            # we round to the closest integer so 3.9999 -> 4
            exponent = round(log((candidate*(base-1)+1), base))
            if candidate == (base**exponent - 1) / (base-1):
                resultSum += candidate
                break
    
    return resultSum

print(findSumStrongRepunits(nonInclusiveLimit = 200))