def getDistinctPrimeDivisors(limit : int):
    distinctPrimesCounter = [0] * ( limit +1)
    for i in range(2, limit):
        if distinctPrimesCounter[i] == 0:
            for j in range(2*i, len(distinctPrimesCounter) , i):
                distinctPrimesCounter[j] += 1
    return distinctPrimesCounter

def get4ConsecutiveDistinctPrimeFactors(distinctPrimeCounter):
    window = [4, 4, 4, 4]
    for i in range(len(distinctPrimeCounter)):
        if window == distinctPrimeCounter[i:i+4]:
            return i
    else:
        return -1
distinctPrimeCounter = getDistinctPrimeDivisors(10**6)
print(get4ConsecutiveDistinctPrimeFactors(distinctPrimeCounter))