'''
    N X N의 격자판
    각각의 칸은 (r, c)로 표현
        - r : 행의 번호 (1 <= r <= N)
        - c : 열의 번호 (1 <= c <= N)
        - 빈 칸(0)이거나 벽(1)이다.
    파이프는 2개의 연속된 칸을 차지함
        - 가로 세로 대각선
    가장 처음 파이프는 (1,1)과 (1,2)를 차지하고 있고 방향은 가로
    파이프의 한쪽 끝을 (N,N)로 이동시키는 방법의 개수를 구하라.
    
    입력
        1. N - 집의 크기 (3 <= N <= 16)
        2. 집에 대한 정보
        
    출력
        - 파이프의 한쪽 끝을 (N,N)으로 이동시키는 방법의 수를 출력
        - 이동시킬 수 없는 경우에는 0을 출력

'''

dr = [0, 1, 1]
dc = [1, 0, 1]

direction = {
    'w' : (0, 2),
    'h' : (1, 2),
    'd' : (0, 1, 2),
}

def path(row, col):
    global count

    state = house[row][col]             # 현재 칸의 방향 문자만 읽기
    for i in direction[state]:
        nr, nc = row + dr[i], col + dc[i]
        if nr >= N or nc >= N:
            continue

        # 빈칸(0) 판정 통일
        if i == 0:  # 가로 이동: 오른쪽 칸만 0이어야 함
            if house[row][col+1] != 0:
                continue
        elif i == 1:  # 세로 이동: 아래 칸만 0이어야 함
            if house[row+1][col] != 0:
                continue
        else:  # 대각 이동: 오른쪽/아래/오른쪽아래 3칸 모두 0
            if not (house[row][col+1] == 0 and house[row+1][col] == 0 and house[row+1][col+1] == 0):
                continue

        if nr == N-1 and nc == N-1:
            count += 1
            continue

        # 다음 칸만 기록 -> 재귀 -> 원복 (현재 칸은 절대 수정 X)
        # prev = house[nr][nc]  # 원래 값 저장

        # i: 0=가로('w'), 1=세로('h'), 2=대각('d')
        if i == 0:
            house[nr][nc] = 'w'
        elif i == 1:
            house[nr][nc] = 'h'
        else:
            house[nr][nc] = 'd'

        path(nr, nc)
        house[nr][nc] = 0  # 원복


N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]
house[0][0], house[0][1] = 'w', 'w'
# print(house)
count = 0
path(0, 1)
print(count)

