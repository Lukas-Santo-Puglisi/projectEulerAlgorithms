
from typing import Set

pandigitials = []
pandigitalSetCond = set([str(i) for i in range(1, 10)])

for countDigit in range(1, 5):
    candidate = 10**(countDigit -1)
    n = 6 - countDigit
    for candidate in range(10**(countDigit -1), 10**(countDigit)):
        digitSet: Set[str] = set()
        concatenated_candidate = ''
        for i in range(n):
            concatenated_candidate = concatenated_candidate + str(candidate*(i+1))
            digitSet.update(list(str(candidate*(i+1))))
        if digitSet == pandigitalSetCond and len(concatenated_candidate)==9:
            pandigitials.append(int(concatenated_candidate))

print(max(pandigitials))

