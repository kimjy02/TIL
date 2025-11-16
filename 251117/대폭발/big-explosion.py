n, m, r, c = map(int, input().split())
from collections import deque
# Please write your code here.

arr = [[0] * n for _ in range(n)]
start_i, start_j = r - 1, c - 1

bombs = [(start_i, start_j)]
arr[start_i][start_j] = 1
time = 0

while True:
    if time >= m:
        break

    time += 1
    new_bombs = []

    for i, j in bombs:
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di * (2 ** (time-1)), j + dj * (2 ** (time-1))
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    new_bombs.append((ni, nj))
    bombs.extend(new_bombs)

print(len(bombs))