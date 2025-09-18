def fibo_dp(n):
    if n == 1:
        return [0, 1]

    if n == 0:
        return [1, 0]

    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n-1:n+1]


T = int(input())
for _ in range(T):
    n = int(input())
    print(*fibo_dp(n))