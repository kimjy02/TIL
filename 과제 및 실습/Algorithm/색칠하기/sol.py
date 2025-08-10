'''
    인덱스가 있는 10 X 10 격자에 빨간색과 파란색을 칠하려고 함
    N개의 영역에 대해 왼쪽 위 / 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
    칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
    입력
        - 테스트 케이스 개수 T
        - 테스트케이스의 첫 줄에 칠할 영역의 개수 N
        - 왼쪽 위 모서리 인덱스 (r1, c1) / 오른쪽 아래 모서리 (r2, c2)와 색상 정보
        - color = 1(빨강), color = 2(파랑)
    출력
        - #T answer
'''

import sys
sys.stdin = open('sample_input.txt')

def color_insert(r1, c1, r2, c2, color):
    global grid
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if grid[i][j] == color or grid[i][j] == 3:
                pass
            else:
                grid[i][j] += color
            # print(f'{i} {j} {grid[i][j]}')

T = int(input())  # 테스트 케이스 개수
for tc in range(1, T+1):
    grid = [[0]*10 for i in range(10)]
    N = int(input())  # 칠할 영역의 개수
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        color_insert(r1, c1, r2, c2, color)
    cnt = 0
    # print(grid)
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')

