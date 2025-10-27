#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

direction = {
    0 : 0,
    1 : 1,
    2 : 2,
    3 : 3
}
right_direction = {
    0 : 3,
    1 : 0, 
    2 : 1,
    3 : 2
}

reverse_direction = {
    0 : 2,
    1 : 3,
    2 : 0,
    3 : 1
}

N, M = map(int, input().split())

position = list(map(int, input().split()))
i, j, direct = position[0], position[1], position[2]
grid = [list(map(int, input().split())) for _ in range(N)]

# print(grid)

def clean(i, j):
    global count
    if 0 <= i <= (N-1) and 0 <= j <= (M-1) and grid[i][j] == 0:
        grid[i][j] = 1
        count += 1

    else:
        for r, c in zipss(dr, dc):
            nr = i + r
            nc = j + c
            if 0 <= i <= (N-1) and 0 <= j <= (M-1) and grid[nr][nc] == 0:
                direct = right_direction[direct]
                nr = nr + dr[direct]
                nc = nc + dc[direct]
                grid[nr][nc] = 1
                return clean(nr, nc)
            
        i = i + dr[right_direction[direct]]
        j = j + dc[right_direction[direct]]
        if 0 <= i <= (N-1) and 0 <= j <= (M-1):
            return clean(i, j)
        else :
            return

count = 0
clean(i, j)
print(count)