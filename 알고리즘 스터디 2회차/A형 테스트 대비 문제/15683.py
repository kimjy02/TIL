#    상  하  좌  우
dr = {-1, 1, 0, 0}
dc = {0, 0, -1, 1}

numbering = {
    1 : [0, 1, 2, 3],
    2 : [[0, 1], [2, 3]],
    3 : [[0, 2], [1, 2], [1, 3], [0, 3]],
    4 : [[2, 3, 0], [2, 3, 1], [2, 3, 1], [2, 3, 0]],
    5 : [[0, 1, 2, 3]]
}

N, M = map(int, input().split())
grid = list(map(int, input().split()))

def direction(i, j):
    if grid[i][j] == 1:


# for i in range(N) :
#     for j in range(M) :
#         if grid[i][j] == 