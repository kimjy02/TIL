N = int(input())

A = list(map(int, input().split()))
dp = [1] * len(A)



for i in range(1, len(A)):
    for j in range(len(A)):
        if j < i and A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
            # print(dp)

print(max(dp))
