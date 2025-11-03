import itertools, copy
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

max_zero_count = 0
zero_check = []
two_check = []

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            zero_check.append((i, j))
        elif grid[i][j] == 2:
            two_check.append((i, j))

for walls in itertools.combinations(zero_check, 3):
    temp = copy.deepcopy(grid)

    # 벽 세우기
    for r, c in walls:
        temp[r][c] = 1

    # 바이러스 확산
    queue = deque(two_check)
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and temp[nr][nc] == 0:
                temp[nr][nc] = 2
                queue.append((nr, nc))

    # 안전영역 세기
    zero_count = sum(row.count(0) for row in temp)
    max_zero_count = max(max_zero_count, zero_count)

print(max_zero_count)
