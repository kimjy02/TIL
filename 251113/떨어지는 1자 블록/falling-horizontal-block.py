n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
grid_t = [list(row) for row in zip(*grid)]
min_index = n

for i in range(k-1, k+m-1):
    for j in range(n):
        if grid_t[i][j] == 1:
            min_index = min(min_index, j)

for idx in range(k-1, k+m-1):
    grid[min_index-1][idx] = 1

for lst in grid:
    print(*lst)