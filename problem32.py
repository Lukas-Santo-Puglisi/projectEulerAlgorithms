import itertools

def findAllUnusuals():
    allDigits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    products = set()
    count = 0
    for combination in itertools.permutations(allDigits, 9):
        multiplierList = combination[0:2]
        multiplierNumber= listToNumber(multiplierList)
        multiplicandList = combination[2:5]
        multiplicandNumber = listToNumber(multiplicandList)
        productList = combination[5:9]
        productNumber = listToNumber(productList)
        if multiplierNumber * multiplicandNumber == productNumber:
            if productNumber not in products:
                count += productNumber
                products.add(productNumber)
    
    return count

def listToNumber(listContainingNumbers):
    result = 0
    
    for index, value in enumerate(listContainingNumbers):
        result += value * 10**(index-1)
    return result



