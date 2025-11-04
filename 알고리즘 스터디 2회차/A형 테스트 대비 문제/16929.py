from collections import deque

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        q = deque()
        q.append((i, j, -1, -1))
        visited = [[False]*M for _ in range(N)]
        visited[i][j] = True

        while q:
            r, c, pr, pc = q.popleft()

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    if grid[nr][nc] == grid[r][c]:
                        # 이전 칸으로 돌아가는 건 무시
                        if nr == pr and nc == pc:
                            continue
                        if visited[nr][nc]:
                            print("Yes")
                            exit()
                        visited[nr][nc] = True
                        q.append((nr, nc, r, c))

print("No")

