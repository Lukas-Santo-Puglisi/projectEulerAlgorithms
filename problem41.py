# only the digit sum of 4-pandig and 7-pandig not divisible by three. 

from itertools import permutations
from math import sqrt

def isPrime(candidate: int)-> bool:
    for i in range(2, int(sqrt(candidate))+1, 1):
        if candidate % i == 0:
            return False
        
    else: 
        return True

max_n_pandig = 0

for permutation in permutations(set((1, 2, 3, 4, 5, 6, 7)), 7):
    if permutation[-1] % 2 != 0:
        candidate = 0
        for i in range(0, len(permutation)):
            candidate += 10**i * permutation[i]
        if isPrime(candidate):
            max_n_pandig = max(candidate, max_n_pandig)

print(max_n_pandig)

