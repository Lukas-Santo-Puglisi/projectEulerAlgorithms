import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

cached_primes = set()

def goldbachs(x):
    global cached_primes
    for i in range(1, x):
        candidate_prime = x - 2 * i**2
        if candidate_prime < 2:
            break
        if candidate_prime in cached_primes or is_prime(candidate_prime):
            cached_primes.add(candidate_prime)
            return True
    return False

i = 33
while True:
    if not is_prime(i) and not goldbachs(i):
        break
    i += 2  

print(i)
