from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            shark_r, shark_c = i, j
            grid[i][j] = 0
            break

shark_size = 2
eat_count = 0
total_time = 0

def search(start_r, start_c, size):
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 0
    fish_list = []

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:

                if grid[nr][nc] <= size:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

                    if 0 < grid[nr][nc] < size:
                        fish_list.append((visited[nr][nc], nr, nc))
    
                        # print(fish_list)

    if not fish_list:
        return None
    fish_list.sort()
    return fish_list[0]

while True:
    target = search(shark_r, shark_c, shark_size)
    if target is None:
        break

    dist, fish_r, fish_c = target
    total_time += dist
    eat_count += 1
    grid[fish_r][fish_c] = 0
    shark_r, shark_c = fish_r, fish_c

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(total_time)
