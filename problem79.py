#for my solution to work we must assume that the digits in the password are unique. If the maximum of the repeats of any number is greater than one but not greater than the keylog length we can solve this problem by constructing a directed graph and get the topological sort. I would assume that it is not possible to deterministically derive the password if the keylog length smaller than the max repeat of any number

from typing import List, Set, Dict

def getKeyLogs(inputPath:str = 'problem79Input.txt')-> List[List[str]]:
    
    keylogs: List[List[str]] = []
    with open(inputPath, 'r') as inputFile:
        for line in inputFile:
            login = list(line)
            keylogs.append(login)
    return keylogs

def createDigitToFollowerDict(keyLogs: List[List[str]])-> Dict[str, Set]:
    followerDict: Dict[str, Set] = {}
    for login in keyLogs:
        if login[0] not in followerDict:
            followerDict[login[0]] = set()
        if login[1] not in followerDict:
            followerDict[login[1]] = set()
        if login[2] not in followerDict:
            followerDict[login[2]] = set()
        followerDict[login[0]].add(login[1])
        followerDict[login[0]].add(login[2])
        followerDict[login[1]].add(login[2])
    print(followerDict)
    return followerDict

def findPassword(followerDict: Dict[str, Set])-> str:
    password = ''
    processedDigits: Set = set()
    for digit in followerDict:
        if followerDict[digit] == {}:
            processedDigits.add(digit)
            password = digit
            del followerDict[digit]
            break
    while followerDict: # empty dicts are falsy 
        for digit in followerDict:
                if followerDict[digit].issubset(processedDigits):
                    password = digit + password
                    processedDigits.add(digit)
                    del followerDict[digit]
                    break
    return password


keylogs = getKeyLogs()
followerDictionary = createDigitToFollowerDict(keylogs)
print(findPassword(followerDictionary))




