N = int(input())

T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())


dp = [0] * (N + 1)

for i in range(N):
    # 1) 오늘 상담 안 하고 내일로(최댓값 전파)
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 2) 오늘 상담하는 경우(가능할 때만)
    end = i + T[i]
    if end <= N:
        dp[end] = max(dp[end], dp[i] + P[i])


# print(dp)
print(dp[N])
