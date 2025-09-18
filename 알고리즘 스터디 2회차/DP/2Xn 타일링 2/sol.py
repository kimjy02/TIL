n = int(input())


def function(n):
    dp = [0] * (n+1)
    if n == 1:
        return 1

    dp[1] = 1
    dp[2] = 3

    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + 2 * dp[i-2]

    return dp[n] % 10007

print(function(n))