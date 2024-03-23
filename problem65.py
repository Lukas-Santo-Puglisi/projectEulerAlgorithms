from typing import List
from fractions import Fraction


def generateListE(n :int = 99) -> List[int]:
    count = 1
    resultList = []
    for i in range(0, n, 1): 
        if i % 3 == 1:
            resultList.append(count*2)
            count +=1
        else:
            resultList.append(1)
    return resultList

def findSumNumeratorNthConvergentOfE(n: int = 99) -> int:
    
    backwardsList = generateListE(n-1)
    if not backwardsList:
        return 2
    val = (backwardsList[-1])**(-1)
    for i in range(len(backwardsList)-2, -1, -1):
        val = (backwardsList[i] + val)**(-1)
    val = val + 2
    fraction_representation = Fraction(val).limit_denominator()
    resultSum = 0
    for character in str(fraction_representation.numerator):
        resultSum += int(character)
    return resultSum


print(findSumNumeratorNthConvergentOfE(100))