import sys

input = sys.stdin.readline

N = int(input())

T = [0] * N
P = [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * (N + 1)  # dp[i] = i일 시작 전까지 얻을 수 있는 최대 이익

for i in range(N):
    # 건너뛰기
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담하기
    if i + T[i] <= N:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(dp[N])
