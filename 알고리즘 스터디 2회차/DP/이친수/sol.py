'''
    이진수 : 0과 1로 이루어진 수
    이친수 : 이진수 중 특별한 성질을 갖는 것
        1. 0으로 시작하지 않음
        2. 1이 두 번 연속 나타나지 않음

    [입력]
        1 <= N <= 90

    [출력]
        N자리 이친수의 개수
'''

N = int(input())

def fibo_dp(N):
    dp = [0] * (N+1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[N]

print(fibo_dp(N))