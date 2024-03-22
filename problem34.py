from math import factorial as fac


def sumFactorialDigits():
    resultSum = 0
    upperLimit = 10**(findAppopriateK())
    
    for i in range(3, upperLimit):
        temp = 0
        candidateCuriousNumber = i
        while candidateCuriousNumber > 0:
            lowestDigit = candidateCuriousNumber % 10
            candidateCuriousNumber //= 10
            temp += fac(lowestDigit)

        if temp == i:
            resultSum += i

    return resultSum

def findAppopriateK():
    k = 1
    while k * fac(9) > 10**k:
        k += 1
    return k