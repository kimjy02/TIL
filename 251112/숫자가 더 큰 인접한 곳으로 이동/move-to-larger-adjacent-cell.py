n, r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
r, c = r - 1, c - 1
result = [a[r][c]]
find = True

while True:
    if find == False:
        break

    find = False
    now = a[r][c]

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = r + di, c + dj
        if 0 <= ni < n and 0 <= nj < n and now < a[ni][nj]:
            result.append(a[ni][nj])
            r, c = ni, nj
            find = True

print(*result)