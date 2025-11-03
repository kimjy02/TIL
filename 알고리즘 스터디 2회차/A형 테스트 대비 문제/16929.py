from collections import deque

N, M = map(int, input().split())

grid = [list(map(str, input().strip())) for _ in range(N)]
# print(grid)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def pathing(i, j):
    global path
    p, q = path[-1]
    for r, c in zip(dr, dc):
        nr = r + p
        nc = c + q
        if 0 <= nr < N and 0 <= nc < M:
            



for i in range(N):
    for j in range(M):
        path = []
        path.append([i, j])
        pathing(i, j)

# path = deque()
# for i in range(N):
#     for j in range(M):
#         visited = [[False] * M for _ in range(N)]
#         path.append([i, j])
#         visited[i][j] = True
#         line = []
#         # print(visited)
#         while path:
#             line.append(path.pop())
#             print(line)
#             p, q = line[-1]
#             length = len(line)
#             for r, c in zip(dr, dc) :
#                 nr = p + r
#                 nc = q + c
#                 # print(nr, nc)
#                 if 0 <= nr < N and 0 <= nc < M:
#                     if grid[p][q] == grid[nr][nc] : 
#                         if not visited[nr][nc]:
#                             path.append([nr, nc])
#                             visited[nr][nc] = True
                        
#                         if len(line) >= 4 and nr == i and nc == j:
#                             print('Yes')
#                             exit()
#                             # break
                    
#                     else:
#                         pass
                    
#             if length == len(line):
#                 break

# print('No')
            

