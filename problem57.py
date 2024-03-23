#step 1: find recurrence condition for (de)nominator
#step 2: implement it

def squareRootDeNominatorCompare(nthExpansionLimit: int = 1000)-> float:
    numeratorLongerDenominatorCount = 0
    nthNominator = 3
    nthDenominator = 2

    for i in range(2, nthExpansionLimit+1, 1):
        # we do simultanous variable assignment not creating immutable tuples 
        nthNominator, nthDenominator = 2*nthDenominator + nthNominator, nthNominator+ nthDenominator
        if len(str(nthNominator)) > len(str(nthDenominator)):
            numeratorLongerDenominatorCount += 1

    return numeratorLongerDenominatorCount / nthExpansionLimit

print(squareRootDeNominatorCompare())