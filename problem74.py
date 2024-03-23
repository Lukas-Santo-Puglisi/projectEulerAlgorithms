
from math import factorial
from typing import Dict

factorial_cache = [factorial(i) for i in range(10)]

def sum_factorial_digits(n: int) -> int:
    return sum(factorial_cache[int(digit)] for digit in str(n))

chain_length_cache : dict[int, int] = {}  # Cache for storing chain lengths

def find_chain_length(start: int) -> int:
    original_start = start
    seen = []
    while start not in seen and start not in chain_length_cache:
        seen.append(start)
        start = sum_factorial_digits(start)
    
    # If we hit a cached value, we use its chain length.
    # Otherwise, it means we've encountered a loop, and the chain length is len(seen).
    if start in chain_length_cache:
        total_chain_length = chain_length_cache[start] + len(seen)
    else:
        total_chain_length = len(seen)
    
    # Update the cache for each value in the seen list with the total chain length.
    for val in seen:
        chain_length_cache[val] = total_chain_length
    
    # For values that are part of the loop and already in the cache, adjust their lengths.
    if start not in chain_length_cache:
        loop_start_index = seen.index(start)
        for i, val in enumerate(seen[loop_start_index:]):
            chain_length_cache[val] = len(seen) - loop_start_index

    return chain_length_cache[original_start]


def count_chains_with_length(limit, target_length):
    count = 0
    for i in range(1, limit):
        if find_chain_length(i) == target_length:
            count += 1
    return count

# Optimized calculation
print(count_chains_with_length(10**6, 60))
