from math import sqrt
from decimal import getcontext, Decimal

def isSquare(candidate: int)->bool:
    return int(round(sqrt(candidate)))**2 == candidate


def digitSumsFirst100NaturalNumbers()->int:
    getcontext().prec = 110
    resultSum = 0
    for naturalNumber in range(1, 101, 1):
        if isSquare(naturalNumber):
            continue
        numberObjectRoot = Decimal(naturalNumber).sqrt()
        firstHundredDigts = str(numberObjectRoot)[0] + str(numberObjectRoot)[2:101]
        digitSum = sum([int(digit) for digit in firstHundredDigts])
        resultSum += digitSum
    return resultSum


print(digitSumsFirst100NaturalNumbers())
