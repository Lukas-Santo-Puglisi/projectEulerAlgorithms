import math

def sum_of_largest_square_divisors(N):
    """
    Calculates the sum of the largest square divisors for all integers up to N,
    where each term in the sum is weighted by the number of integers for which
    it is the largest square divisor. The result is returned modulo 1,000,000,007.

    Args:
    N (int): The upper limit of the range of integers to consider.

    Returns:
    int: The sum of largest square divisors modulo 1,000,000,007.
    """

    # Calculate the square root of N, rounded down to the nearest integer.
    # This value represents the maximum possible value for i where i*i can be
    # a divisor of numbers up to N.
    sqrtN = int(math.sqrt(N))

    # Initialize the array 'a' with 0 at index 0 and 1 for indices 1 to sqrtN.
    # This setup is for counting the number of integers up to N for which each
    # square (i*i) is the largest square divisor, starting with the assumption
    # that each square can be a divisor (hence initializing with 1).
    a = [0] + [1]*sqrtN

    # Iterate over each potential square divisor starting from sqrtN down to 1.
    # This reverse iteration ensures that when we consider a square i*i, we have
    # already accounted for all larger squares that could also divide the integers
    # up to N, allowing to adjust counts.
    for i in range(sqrtN, 0, -1):
        # Calculate the initial count of integers divisible by i*i (up to N),
        # then subtract the counts for all larger squares that are multiples of i*i.
        # This subtraction removes overlaps and ensures 'a[i]' reflects
        # the count of numbers for which i*i is the largest square divisor.
        a[i] = math.floor(N/(i*i)) - sum([a[i*j] for j in range(2, math.floor(sqrtN/i) + 1)])

    # Calculate the sum of i*i*a[i] for all i, where i*i represents the square
    # and a[i] the count of integers for which this square is the largest square divisor.
    # The sum is computed modulo 1,000,000,007 to handle large numbers.
    return (sum([i*i*a[i] for i in range(len(a))])) % 1_000_000_007

N = 30
print(sum_of_largest_square_divisors(N))
