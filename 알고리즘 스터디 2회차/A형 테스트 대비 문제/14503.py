#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 방향 왼쪽 회전 (시계 반대)
left_dir = {
    0: 3,
    1: 0, 
    2: 1, 
    3: 2
}

# 뒤로 가기
back_dir = {
    0: 2, 
    1: 3, 
    2: 0, 
    3: 1
}

N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

count = 0

def clean(r, c, d):
    global count

    # 1. 현재 위치 청소
    if grid[r][c] == 0:
        grid[r][c] = 2  # 청소 표시
        count += 1

    # 2. 4방향 탐색
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 방향으로 회전
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
            clean(nr, nc, d)
            return  # 한 방향으로 이동했으면 그 다음 탐색은 거기서 다시 시작

    # 3. 4방향 모두 청소 or 벽일 경우, 뒤로 이동
    back = back_dir[d]
    br = r + dr[back]
    bc = c + dc[back]
    if 0 <= br < N and 0 <= bc < M and grid[br][bc] != 1:
        clean(br, bc, d)
    else:
        return

clean(r, c, d)
print(count)
