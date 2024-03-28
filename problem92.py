
def getSquareOfDigit(digit: int) -> int:
    return sum(int(x)**2 for x in str(digit))


def findEnd(x):
    while True:
        x = getSquareOfDigit(x)
        if x == 89:
            return 89
        if x == 1:
            return 1

def giveCount(limit):
    count = 0
    mem = [0] + [findEnd(x) for x in range(1,len(str(limit)) * 9**2)]     
    for y in range(1,limit + 1):
        memedVal = mem[getSquareOfDigit(y)]
        if memedVal == 89:
            count += 1    
    return count

print(giveCount(100))


