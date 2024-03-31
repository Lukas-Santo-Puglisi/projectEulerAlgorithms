from math import sqrt
from typing import Set, Tuple

def isPrime(candidate: int)->bool:
    if candidate == 1:
        return False
    if candidate == 2:
        return True
    for i in range(2, int(sqrt(candidate))+1):
        if candidate % i == 0: 
            return False
    else:
        return True


def countSpiralPrimes()-> int:
    count = 0
    br = n = 1 #bottom right, sidelength
    diagonals = 1
    while ((count / diagonals) >= 0.1 or n<=7):
        diagonals += 4
        n += 2
        for i in range(1, 5):
            if isPrime(br + i * (n - 1)):
                count += 1
        br = br + 4*(n-1)
    return n
        

print(countSpiralPrimes())


