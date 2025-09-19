T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1 or N == 2 or N == 3:
        print(1)
    else:
        dp = [0] * N
        dp[0], dp[1], dp[2] = 1, 1, 1

        for i in range(3, N):
            dp[i] = dp[i-3]+dp[i-2]

        print(dp[N-1])


