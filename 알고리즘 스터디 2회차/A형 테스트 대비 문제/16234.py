# import sys
# sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())
# print(N, L, R)
grid = [list(map(int, input().split())) for _ in range(N)]
# print(grid)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def search(i, j):
    global population, check

    stack = [[i, j]]    
    visited[i][j] = True

    while stack :
        p, q = stack.pop()
        population += grid[p][q]
        check.append([p, q])
        for r, c in zip(dr, dc):
            nr = r + p
            nc = c + q
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(grid[p][q] - grid[nr][nc]) <= R:
                    visited[nr][nc] = True
                    stack.append([nr, nc])
        # print(check)
    return

def cnt():
    global population, counting

    if len(check) > 1 :
        population //= len(check)
        for i, j in check:
            grid[i][j] = population  
        counting += 1
        # print(grid)
    return

count = 0
while True:
    visited = [[False] * N for _ in range(N)]
    counting = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: 
                population = 0
                check = []
                search(i, j)
                cnt()
    if counting > 0:
        count += 1
        # print(count)
    else:
        break
print(count)