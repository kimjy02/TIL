method = {
    # 정사각형
    0 : [[0, 1], [1, 0], [1, 1]],
    # ㄴ 모양
    1 : [[1, 0], [2, 0], [2, 1]],
    2 : [[1, 0], [1, 1], [1, 2]],
    3 : [[0, 1], [1, 1], [2, 1]],
    4 : [[0, 1], [1, 0], [0, 2]],
    # 테트리스 모양
    5 : [[1, 0], [1, 1], [2, 1]],
    6 : [[0, 1], [1, -1], [1, 0]],
    7 : [[1, 0], [1, -1], [2, -1]],
    8 : [[0, 1], [1, 1], [1, 2]],
    # ㅜ 모양
    9 : [[0, 1], [0, 2], [1, 1]],
    10 : [[1, 0], [1, 1], [2, 0]],
    11 : [[1, -1], [1, 0], [1, 1]],
    12 : [[1, 0], [1, -1], [2, 0]],
    # ㅣ 모양
    13 : [[0, 1], [0, 2], [0, 3]],
    14 : [[1, 0], [2, 0], [3, 0]], 
    # 추가
    15 : [[0, 1], [1, 0], [2, 0]],
    16 : [[0, 1], [0, 2], [1, 2]],
    17 : [[1, 0], [2, 0], [2, -1]],
    18 : [[1, 0], [1, -1], [1, -2]]
}

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

# for m in method.values():
#     print(m)
max_value = 0
for i in range(N):
    for j in range(M):
        for m in method.values():
            value = 0
            value += grid[i][j]
            for r, c in m:
                nr = i + r
                nc = j + c
                # print(nr, nc)
                if 0 <= nr <= (N-1) and 0 <= nc <= (M-1):
                    value += grid[nr][nc]
                else:
                    continue
           
            # print(value)
            max_value = max(max_value, value)

print(max_value)