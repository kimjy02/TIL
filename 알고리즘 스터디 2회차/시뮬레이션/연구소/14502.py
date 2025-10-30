import itertools
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

# print(grid)

max_zero_count = 0
zero_check = []
two_check = deque()
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            zero_check.append([i,j])
        
        if grid[i][j] == 2:
            two_check.append([i, j])
            visited[i][j] = True
        
        if grid[i][j] == 1:
            visited[i][j] = True       

wall_add = list(itertools.combinations(zero_check, 3))
# print(len(wall_add))
for tup in wall_add:
    visited = [[False] * M for _ in range(N)]
    for lst in tup:
        grid[lst[0]][lst[1]] = 1
    
    while two_check:
        i, j = two_check.popleft()
        for r, c in zip(dr, dc):
            nr = r + i
            nc = c + j
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                two_check.append([nr,nc])
    
    zero_count = 0
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False:
                zero_count += 1
        
    max_zero_count = max(max_zero_count, zero_count)
    

print(max_zero_count)
    # print(tup)

# print(zero_check)
                

