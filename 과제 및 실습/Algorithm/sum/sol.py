'''
    다음 100 X 100의 2차원 배열이 주어질 때,
    각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램 작성하라.
    제약 조건
        - 총 10개의 테스트 케이스
        - 배열의 크기 : 100 X 100
        - 각 행의 합은 integer 범위를 넘어가지 않음
        - 동일한 최댓값이 있을 경우, 하나의 값만 출력
    입력
        - 테스트 케이스 번호
        - 2차원 배열의 각 행 값 [100개씩 100줄 입력]
    출력
        - # 부호와 함께 테스트 케이스 번호 출력 / 테스크 케이스 답 출력
'''
import sys
sys.stdin = open('input.txt')

def row_sum(row):
    global max_sum
    if row <= 99:
        total = 0
        for i in range(100):
            total += arr[row][i]
        max_sum = max(max_sum, total)
        # print(f'{i+1} {max_sum}')
        row_sum(row+1)

    if row > 99:
        return

def col_sum(col):
    global max_sum
    if col <= 99:
        total = 0
        for i in range(100):
            total += arr[i][col]
        max_sum = max(max_sum, total)
        # print(f'{i+1} {max_sum}')
        col_sum(col+1)

    if col > 99:
        return

for _ in range(10):
    N = int(input())  # 테스트 케이스 번호
    arr = []
    max_sum = 0
    for _ in range(100):
        line = list(map(int, input().split()))
        arr.append(line)
    row_sum(0)
    col_sum(0)
    total = 0
    for i in range(100):
        total += arr[i][i]
    max_sum = max(total, max_sum)
    # print(max_sum)
    total = 0
    for i in range(100):
        # print(arr[i][99-i])
        total += arr[i][99-i]
    max_sum = max(total, max_sum)
    # print(max_sum)
    print(f'#{N} {max_sum}')