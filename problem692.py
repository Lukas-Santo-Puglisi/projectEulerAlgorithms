from typing import Dict, Tuple

def isWinning(heapSize: int, prevPlayer:int, mem: Dict[Tuple[int, int], bool])-> bool:
    if (heapSize, prevPlayer) in mem:
        return mem[heapSize, prevPlayer]
    if heapSize == 0:
        mem[heapSize, prevPlayer] = False
        return False
    if heapSize <= 2* prevPlayer:
        mem[heapSize, prevPlayer] = True
        return True
    playerWinning = False
    
    for player in range(1, 2*prevPlayer+1, 1):
        prevWinning = isWinning(heapSize-player, player, mem)
        if not prevWinning:
            playerWinning = True
    
    mem[heapSize, prevPlayer] = playerWinning

    return playerWinning

def findMinimalAmountToTake(heapSize: int)-> int:
    minimumAmount = heapSize
    for player in range(1, heapSize+1):
        mem: Dict[Tuple[int, int], bool] = {}
        if not isWinning(heapSize-player, player, mem):
            minimumAmount = player
            break
    return minimumAmount

def sumMinimumAmounts(heapSizeLimit: int)-> int:
    resultSum = 0
    for heapSize in range(1, heapSizeLimit +1):
        resultSum += findMinimalAmountToTake(heapSize)
    return resultSum
    
print(sumMinimumAmounts(80))

