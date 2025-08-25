'''
    일정액을 내면 크기가 정해진 박스가 가득 찰 때까지 마음대로 물건을 골라 담을 수 있는 해피박스 이벤트가 열린다고 한다.
    박스에 담긴 물건의 가격합계가 최대가 되도록 물건을 담으려고 한다.
    담을 수 있는 물건 가격은 최대 얼마인지 알아내는 프로그램을 작성하시오.
    담긴 상품 크기의 합이 박스 크기를 초과할 수 없음
    각 상품은 1개씩 있음
    예: 박스 크기가 10이고 상품의 크기와 가격이 다음과 같다면,
    최대로 담을 수 있는 가격 합계는 2, 3번을 담았을 때인 25이다.
      상품    크기    가격
       1       6      12
       2       5      10
       3       5      15
       4       4       6

    입력
        1. T : 테스트 케이스 수
        2. N : 박스의 크기 / M : 상품의 개수 (10 <= N <= 100)
        3. S_i : 상품 i의 크기 / P_i: 상품 i의 가격 (1 <= S_i, P_i, M <= 20)

    출력
        - #{tc} {담을 수 있는 물건의 최대 가격}
'''
# import sys
# sys.stdin = open('sample_input.txt')

def knapsack_optimized(weight, values, N):
    dp = [0] * (N+1)

    for i in range(len(weight)):
        for w in range(N, weight[i] - 1, -1):
            dp[w] =max(dp[w], values[i] + dp[w - weight[i]])

    return dp[N]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight, values = [0 for _ in range(M)], [0 for _ in range(M)]
    for i in range(M):
        weight[i], values[i] = map(int, input().split())
    max_value = knapsack_optimized(weight, values, N)
    print(f'#{tc} {max_value}')




