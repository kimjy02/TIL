'''
    N X N 크기의 농장
    규칙
        1. 농장의 크기는 항상 홀수
        2. 수확은 항상 농장의 크기에 맞는 정사각형 마름모 형태로만 가능
        3. 수익
            - 1 X 1 크기의 농장에서 자라는 농작물을 수확해 얻을 수 있는 수익 : 3
            - 3 X 3 크기의 농장에서 자라는 농작물을 수확해 얻을 수 있는 수익 :
              : 3+2+5+4+2 = 16
            - 5 X 5 크기의 농장에서 자라는 농작물을 수확해 얻을 수 있는 수익 :
              : 3+2+1+1+2+5+1+1+3+3+2+1 = 25
    농장의 크기 N과 농작물의 가치가 주어질 떄, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구해라

    제약 사항
        - 농장의 크기 N은 1 이상 49 이하의 홀수
        - 농작물의 가치는 0~5이다.

    입력
        - 첫번째 줄 : T - 테스트 케이스 개수
        - 두번째 줄 : N - 테스트 케이스의 농장의 크기
        - 세번째 줄 : 농장 내 농작물의 가치

    출력
        - #{tc} {농장의 규칙에 따라 얻을 수 있는 수익}
'''
# import sys
# sys.stdin = open('input.txt')

def calculator(N, farm, idx):
    total = 0
    for i in range(N):
        reach = idx - abs(idx - i)  # 가운데에서 퍼지는 폭
        print(reach)
        left = idx - reach
        right = idx + reach
        # 슬라이싱 대신 인덱스 합으로 임시 리스트 생성 X
        row_sum = 0
        row = farm[i]
        for j in range(left, right + 1):
            row_sum += row[j]
        total += row_sum
    return total
    # col = 0
    # for i in range(idx, -1, -1):
    #     total += sum(farm[i][col:N-col-1])
    #     # print(f'{i} {col} {total}')
    #     col += 1
    # col = 0
    # for i in range(idx+1, N):
    #     total += sum(farm[i][col:N-col-1])
    #     # print(total)
    #     col += 1
    # return total

T = int(input())    # T : 테스트 케이스 수
for tc in range(1, T+1):
    N = int(input())    # N : 농장의 크기
    farm = [list(map(int,input().strip())) for i in range(N)]
    middle = N // 2
    print(f'#{tc} {calculator(N, farm, middle)}')