#first insight is that the difference between two pentagonals is the smallest when they are neighbours. this yields the main insight that P_n+1 - P_n = 2*n + 1, so the difference between two consecutive pentagonal numbers grows by factor 2 -> both insights together proove that the smallest difference between pentagonals up to the n-th pentagonal is the smallest difference between all pentagonals -> search buttom up. function is_pentagonal uses quadratic solution formula

from math import sqrt

def is_pentagonal(x: int):
    n = round( (1 + sqrt(1+ 24*x))/ 6)
    return  3*n**2 - n - 2*x == 0

def find_smallest_difference():
    k = 2
    while True:
        P_k = (k*(3*k -1))//2
        for j in range(k-1, 0, -1):
            P_j = (j*(3*j -1))//2
            if is_pentagonal(P_k + P_j) and is_pentagonal(P_k - P_j):
                return P_k - P_j
        k += 1

print(find_smallest_difference())