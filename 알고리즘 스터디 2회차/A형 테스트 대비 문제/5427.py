from collections import deque

dr = [-1, +1, 0, 0]
dc = [0, 0, -1, +1]

def pathing():
    path = deque()
    visited = [[False] * C for _ in range(R)]
    fire = deque()

    for i in range(R):
        for j in range(C):
            if maze[i][j] == '@':
                path.append([i, j, 0])
                visited[i][j] = True
            
            elif maze[i][j] == '*' :
                fire.append([i, j])
        
    while path:
        
        for _ in range(len(fire)):
            fr, fc = fire.popleft()
            for r, c in zip(dr, dc):
                nr = fr + r
                nc = fc + c
                if 0 <= nr < R and 0 <= nc < C and (maze[nr][nc] == '.' or maze[nr][nc] == '@'):
                    fire.append([nr, nc])
                    maze[nr][nc] = '*'

        for _ in range(len(path)):
            a, b, time = path.popleft()
            for r, c in zip(dr, dc):
                nr = a + r
                nc = b + c
                if 0 <= nr < R and 0 <= nc < C :
                    if maze[nr][nc] == '.' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        path.append([nr, nc, time + 1])

                
                else:
                    print(time + 1)
                    return
        
    print('IMPOSSIBLE')



T = int(input())

for _ in range(T):
    C, R = map(int, input().split())

    maze = [list(map(str, input().strip())) for _ in range(R)]

    pathing()

    