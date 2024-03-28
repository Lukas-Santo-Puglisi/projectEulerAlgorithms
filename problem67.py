from typing import List

def maxPathSum(triangle:List[List[int]])-> int:
    if not triangle:
        return -1
    oldList = [triangle[0][0]]

    for row in range(1, len(triangle)):
        updateList = [ triangle[row][0] + oldList[0]]
        for column in range(1, len(oldList), 1):
            updateList.append(max(oldList[column-1], oldList[column]) + triangle[row][column])
        updateList.append(oldList[-1] + triangle[row][-1])
        oldList = updateList


    return max(oldList)

def convertInputToTriangleList(filepath: str)-> List[List[int]]:
    
    triangle: List[List[int]] =  []
    with open(filepath, 'r') as triangleDate:
        for row in triangleDate:
            rowListWithStrings = row.split(' ')
            rowListWithIntegers = [int(character) for character in rowListWithStrings]
            triangle.append(rowListWithIntegers)
    return triangle

def solveProblem():
    triangle = convertInputToTriangleList('problem67Input.txt')
    maximumSum = maxPathSum(triangle)
    print(maximumSum)

solveProblem()
