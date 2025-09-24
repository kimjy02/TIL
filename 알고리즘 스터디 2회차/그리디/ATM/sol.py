N = int(input())
time = sorted(list(map(int, input().split())))

dp = [0] * N
dp[0] = time[0]

if N == 1:
    print(dp[0])
else:
    for i in range(1, N):
        dp[i] = dp[i-1] + time[i]

# print(dp)
    print(sum(dp))