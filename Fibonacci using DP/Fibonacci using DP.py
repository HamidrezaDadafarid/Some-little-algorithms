def fib(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    if (n > 0):
        dp[1] = 1
    for i in range(2, (n + 1)):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input("Please enter the number of the Fibonacci sequence you want to calculate: "))
print(fib(n))
