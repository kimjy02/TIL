'''
    N X N 격자판으로 나타낼 수 있음
    1 X 1 크기의 정사각형 칸으로 나누어져 있음
    각 칸은 (r,c)로 나타냄 [r : 행의 번호, 1부터 시작 / c : 열의 번호, 1부터 시작]
    파이프 1개 당 2개의 연속된 칸을 차지하는 크기
    파이프 회전 방향 : 가로 세로 대각선
    가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고, 방향은 가로
    파이프의 한쪽 끝을 (N,N)로 이동시키는 방법의 개수를 구해보자

    입력
        - 첫번째 줄 : N - 집의 크기 (3 <= N <= 16)
        - 두번째 줄 : 집의 상태가 주어짐 (빈칸 : 0 / 벽 : 1)
          - (1,1) & (1,2)는 항상 빈칸
          
    출력
        - 한쪽 끝을 (N,N)으로 이동시키는 방법의 수
        - 이동시킬 수 없는 경우에는 0 출력
'''


def width(house, row, col):
    if row+1 <= N and house[row+1][col] != 1:
        house[row+1][col] = 'w'

def length(house, row, col):
    if col+1 <= N and house[row][col+1] != 1:
        house[row][col+1] = 'l'

def diag(house, row, col):
    if row+1 <= N and col+1 <= N and house:
        house[row + 1][col + 1] = 'd'
        house[row + 1][col] = 'd'
        house[row][col + 1] = 'd'









N = int(input())  # N : 집의 크기 (정사각형)
house = [list(map(int, input().split())) for _ in range(N)]
house[0][0], house[0][1] = 'w', 'w'
# print(house)


