from math import gcd

max_n, max_d = 0, 1

for d in range(2, 10**2 + 1):
    # Calculate the numerator based on whether d is divisible by 7
    if d % 7 == 0:
        n = (3*d)//7 - 1
    else:
        n = (3*d)//7
    
    # Check if this fraction is greater than the current maximum and if n and d are coprime
    if n * max_d > max_n * d and gcd(n, d) == 1:
        max_n, max_d = n, d

# Print the maximum numerator found
print(f"The numerator of the fraction immediately to the left of 3/7 for d <= 10^7 is: {max_n}")
