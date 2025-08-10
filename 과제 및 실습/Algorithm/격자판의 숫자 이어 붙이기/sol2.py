'''
    4 X 4 크기의 격자판
    격자판의 각 격자칸에는 0~9 사이의 숫자가 적혀 있다.
    격자판의 임의의 위치에서 시작해서,
    동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서,
    각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7 자리의 수가 된다.

    이동할 때 한 번 거쳤던 격자판을 다시 거쳐도 되며,
    0으로 시작하는 0102001과 같은 수를 만들 수도 있다.

    단, 격자판을 벗어나는 이동은 불가능
    격자판이 주어졌을 때, 만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램 작성

    입력
        - 첫 번째 줄 : T - 테스트 케이스 수
        - 다음 줄 : 4개의 줄에 걸쳐 각 줄마다 4개의 정수로 격자판 정보

    출력
        - #tc 일곱자리 수들의 개수
'''

import sys
sys.stdin = open('sample_input.txt')

direction = [[1,0], [-1,0],[0,1],[0,-1]]  # 좌 우 하 상

def direct(list, row, col):
    global lst

    for i in range(7):
        if 


T = int(input())
for i in range(T):
    grid = [[0]*4 for _ in range(4)]
    # print(grid)
    result = set()
    for i in range(4):
        grid[i] = list(map(int, input().split()))
    # print(grid)
    lst = []
    for row in range(4):
        for col in range(4):
            grid[row][col]












