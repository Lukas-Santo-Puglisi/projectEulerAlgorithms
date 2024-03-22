
from typing import List


def minPathSum(matVal: List[List[int]]) -> int:
    if not matVal or not matVal[0]:
        return 0
    width: int = len(matVal[0]) + 1
    height: int = len(matVal) + 1
    resultArray: List[List[int]] = [ [0]*width for _ in range(height)] 

    for row in range(0, height):
        resultArray[row][0] = float('inf') 
    for col in range(0, width):
        resultArray[0][col] = float('inf')

    resultArray[1][1] = matVal[0][0]

    for row in range(1, height):
        for column in range(1, width):
            if row != 1 or column != 1: 
                resultArray[row][column] = matVal[row - 1][column - 1] + min(resultArray[row - 1][column], resultArray[row][column - 1])
    
    return resultArray[height-1][width-1]


