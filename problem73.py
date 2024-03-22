from math import gcd


def countProperFractionsInInterval(left :float = 1/3, right:float = 1/2, accuracy=12000) -> int:
    count = 0
    for d in range(4, accuracy +1):
        for n in range(1, d//2 +1, 1):
            if gcd(n, d) == 1 and n / d > left and n/d < right:
                count += 1
            
    
    return count

print(countProperFractionsInInterval(accuracy= 12000))