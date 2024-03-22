import math

def isPrime(candidatePrime):
    if candidatePrime < 2:
        return False
    if candidatePrime == 2:
        return True
    for i in range(2, int(math.sqrt(candidatePrime)) + 1, 2):
        if candidatePrime % i == 0:
            return False
    return True

def isRightTruncatable(candidatePrime):
    while candidatePrime > 0:
        if not isPrime(candidatePrime):
            return False
        candidatePrime //= 10
    return True

def findSumTruncatablePrimes():
    foundTruncatablePrimes = 0
    resultSum = 0
    leftTruncatable = [3, 7]  # Start with basic left-truncatable primes

    while foundTruncatablePrimes < 11:
        newLeftTruncatable = []
        for num in leftTruncatable:
            for digit in [1, 3, 7, 9]:  # Digits that can potentially keep the number prime
                candidate = num * 10 + digit
                if isPrime(candidate):
                    # Only add to leftTruncatable if not yet confirming as right-truncatable
                    # to prevent re-checking and ensure we expand on potential candidates
                    if isRightTruncatable(candidate):
                        foundTruncatablePrimes += 1
                        resultSum += candidate
                    else:
                        newLeftTruncatable.append(candidate)
        leftTruncatable = newLeftTruncatable

    return resultSum

# Calculate and print the sum of the 11 truncatable primes
sumTruncatablePrimes = findSumTruncatablePrimes()
print(sumTruncatablePrimes)
