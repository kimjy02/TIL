from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

# 방향 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)

def bfs():
    q = deque()
    q.append((red[0], red[1], blue[0], blue[1], 0))
    visited = set()
    visited.add((red[0], red[1], blue[0], blue[1]))

    while q:
        rr, rc, br, bc, cnt = q.popleft()
        if cnt >= 10:  
            return -1

        for i in range(4):

            nrr, nrc, red_hole, r_move = move(rr, rc, dr[i], dc[i])
            nbr, nbc, blue_hole, b_move = move(br, bc, dr[i], dc[i])


            if blue_hole:
                continue

            if red_hole:
                return cnt + 1

            if nrr == nbr and nrc == nbc:
                if r_move > b_move:
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    nbr -= dr[i]
                    nbc -= dc[i]

            if (nrr, nrc, nbr, nbc) not in visited:
                visited.add((nrr, nrc, nbr, nbc))
                q.append((nrr, nrc, nbr, nbc, cnt + 1))
    return -1

def move(r, c, dr, dc):
    move_count = 0
    while True:
        nr = r + dr
        nc = c + dc
        if board[nr][nc] == '#':
            break
        r, c = nr, nc
        move_count += 1
        if board[nr][nc] == 'O':
            return r, c, True, move_count
    return r, c, False, move_count

print(bfs())
