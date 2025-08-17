dr = [0, 1, 1]   # 0: 가로(→), 1: 세로(↓), 2: 대각(↘)
dc = [1, 0, 1]

direction = {
    'w': (0, 2),      # 가로면 가로/대각
    'h': (1, 2),      # 세로면 세로/대각
    'd': (0, 1, 2),   # 대각이면 가로/세로/대각
}

N = int(input().strip())
house = [list(map(int, input().split())) for _ in range(N)]

count = 0

def path(row, col, state):
    # 전역 lookup 최소화(로컬 바인딩)
    h = house
    ndirs = direction[state]
    r = row; c = col

    for i in ndirs:
        nr = r + dr[i]
        nc = c + dc[i]

        # 이동은 오른쪽/아래/대각 뿐이라 하한 체크 필요 없음(상한만 체크)
        if nr >= N or nc >= N:
            continue

        if i == 0:
            # 가로: 오른쪽 칸만 0이어야 함
            if h[r][c+1]: 
                continue
        elif i == 1:
            # 세로: 아래 칸만 0이어야 함
            if h[r+1][c]:
                continue
        else:
            # 대각: 오른/아래/오른아래 3칸 모두 0 (nr=r+1, nc=c+1 보장됨)
            if h[r][c+1] or h[r+1][c] or h[r+1][c+1]:
                continue

        if nr == N-1 and nc == N-1:
            global count
            count += 1
        else:
            path(nr, nc, 'w' if i == 0 else ('h' if i == 1 else 'd'))

# 시작: (0,1) 끝점, 가로
if house[0][0] == 0 and house[0][1] == 0:
    path(0, 1, 'w')

print(count)