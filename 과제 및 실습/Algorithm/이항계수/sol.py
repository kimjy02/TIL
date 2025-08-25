'''
    n, a, b가 주어지면 (x+y)^n에서 x^a y^b의 계수를 구하는 프로그램을 작성하라.
    예를 들어 n, a, b가 2, 1, 1인 경우 (x+y)^2 = x^2 + 2xy + y^2이 되고, xy의 계수는 2이다.

    입력
        1. T : 테스트 케이스 수
        2. n a b (항상 a+b=n을 만족)
    출력
        -#{tc} {x^a y^b의 계수}
'''
import sys
sys.stdin = open('sample_input.txt')
def bino(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i - 1][j - 1]
    return dp[n][k]

T = int(input())

for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    print(f'#{tc} {bino(n, a)}')
