def coinCombinations(targetNum : int = 200)-> int:
    amounts = [1]*(targetNum+1)
    coins = [2, 5, 10, 20, 50, 100, 200]
    for coin in coins:
        for amount in range(len(amounts)-1, 0, -1):
            for step in range(amount-coin, -1, -coin):
                amounts[amount] += amounts[step]
    return amounts[-1]

print(coinCombinations())