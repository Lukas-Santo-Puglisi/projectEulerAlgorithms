def dynamicCountingSum(target: int):
    dp = [0] * (target + 1)
    dp[0] = 1  
    for num in range(1, target + 1):
        for i in range(num, target + 1):
            dp[i] += dp[i - num]
    return dp[target] - 1  


        
