R, C = map(int, input().split())
grid = [list(map(str, input().strip())) for _ in range(R)]

# print(grid)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'S':
            for r, c in zip(dr, dc):
                nr = r + i
                nc = c + j
                