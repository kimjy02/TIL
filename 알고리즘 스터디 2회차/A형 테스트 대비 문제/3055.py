from collections import deque

R, C = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(R)]

# print(grid)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def pathing():    
    path = deque()
    water = deque()
    visited = [[False] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'S':
                path.append([i, j, 0])
                visited[i][j] = True
            elif grid[i][j] == '*':
                 water.append([i, j])

    while path : 
        
        for _ in range(len(water)):
            wr, wc = water.popleft()
            for r, c in zip(dr, dc) :
                 nr = wr + r
                 nc = wc + c
                 if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '.':
                      grid[nr][nc] = '*'
                      water.append([nr, nc])

        for _ in range(len(path)):
            a, b, time = path.popleft()
            for r, c in zip(dr, dc):
                nr = r + a
                nc = c + b
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] :
                    if grid[nr][nc] == 'D' :
                        print(time + 1)
                        return
                    
                    if grid[nr][nc] == '.' :
                        # grid[nr][nc] = 'X'
                        visited[nr][nc] = True
                        path.append([nr, nc, time+1])

    print('KAKTUS')

pathing()

