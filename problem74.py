
from math import factorial
from typing import Dict

factorial_cache = [factorial(i) for i in range(10)]

def sum_factorial_digits(n: int) -> int:
    return sum(factorial_cache[int(digit)] for digit in str(n))

chain_length_cache : dict[int, int] = {}  # Cache for storing chain lengths

def find_chain_length(start):
    original_start = start
    seen = []
    while start not in seen and start not in chain_length_cache:
        seen.append(start)
        start = sum_factorial_digits(start)
    
    base_length = 0
    if start in chain_length_cache:
        base_length = chain_length_cache[start]

    for i, val in enumerate(reversed(seen)):
        chain_length_cache[val] = i + 1 + base_length
    
    return chain_length_cache[original_start]

def count_chains_with_length(limit, target_length):
    count = 0
    for i in range(1, limit):
        if find_chain_length(i) == target_length:
            count += 1
    return count

# Optimized calculation
print(count_chains_with_length(10**6, 60))
