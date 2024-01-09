def minimum_number_of_coins(coins, m):
    k = len(coins)
    dp = [[0] * (m + 1) for i in range(k + 1)]
    for i in range(m + 1):
        dp[0][i] = float('inf')
    for i in range(1, k + 1):
        dp[i][0] = 0
        for j in range(1, m + 1):
            if (coins[i - 1] > j):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
    return dp[k][m]

coins = [1, 3, 4, 5]
m = 7
print(minimum_number_of_coins(coins, m))


