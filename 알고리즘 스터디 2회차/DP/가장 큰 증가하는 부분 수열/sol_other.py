N = int(input())

A = list(map(int, input().split()))
dp = [0] * len(A)
dp[0] = A[0]


for i in range(1, len(A)):
    for j in range(len(A)):
        if j < i and A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])
            # print(dp)

print(max(dp))
