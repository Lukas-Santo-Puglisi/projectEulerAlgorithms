from functools import reduce
from math import gcd
values = []
for x in range(10, 100):
    for y in range(x+1, 101):
        if str(y).endswith('0'):
            continue
        replicateSet = set(str(x)).intersection(set(str(y)))
        
        if replicateSet:
            replicatedVal = next(iter(replicateSet))
            newX = int(str(x)[0]) if str(x)[0] != replicatedVal else int(str(x)[1])
            newY = int(str(y)[0]) if str(y)[0] != replicatedVal else int(str(y)[1])

            if newX / newY == x / y:
                values.append((x,y))

resultNom = reduce(lambda x,y: x*y[0], values, 1)
resultDen = reduce(lambda x,y: x*y[1], values, 1) 
print(resultDen//gcd(resultNom, resultDen))

