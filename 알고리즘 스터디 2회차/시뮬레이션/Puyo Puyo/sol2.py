from collections import deque

H, W = 12, 6
board = [list(input().strip()) for _ in range(H)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(sr, sc, visited):
    color = board[sr][sc]
    if color == '.':
        return []
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    group = [(sr, sc)]
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and board[nr][nc] == color:
                visited[nr][nc] = True
                q.append((nr, nc))
                group.append((nr, nc))
    return group

def apply_gravity():
    # 각 열에 대해 아래부터 채우기
    for c in range(W):
        write = H - 1
        for r in range(H - 1, -1, -1):
            if board[r][c] != '.':
                board[write][c] = board[r][c]
                if write != r:
                    board[r][c] = '.'
                write -= 1
        # 위쪽 남은 칸을 모두 '.'
        for r in range(write, -1, -1):
            board[r][c] = '.'

chain = 0
while True:
    visited = [[False]*W for _ in range(H)]
    to_burst = set()
    for i in range(H):
        for j in range(W):
            if board[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, visited)
                if len(group) >= 4:
                    to_burst.update(group)

    if not to_burst:
        break  # 더 이상 터질 게 없으면 종료

    # 동시에 제거
    for r, c in to_burst:
        board[r][c] = '.'

    # 중력 적용
    apply_gravity()

    chain += 1

print(chain)
