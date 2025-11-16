n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 값 → (행, 열) 위치 정보 딕셔너리
dct = {}
for i in range(n):
    for j in range(n):
        dct[grid[i][j]] = (i, j)

dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)]  # 8방향

for _ in range(m):
    for x in range(1, n * n + 1):   # 숫자 1 ~ n^2 순서대로
        i, j = dct[x]
        bi, bj = i, j         # 바꿀 위치 (기본은 자기 자신)
        max_value = -1        # 이웃 중 최댓값 (처음엔 -1)

        # 8방향 이웃 중 최댓값 찾기
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] > max_value:
                    max_value = grid[ni][nj]
                    bi, bj = ni, nj

        # 무조건 max_value가 있는 자리와 swap
        other = grid[bi][bj]
        grid[i][j], grid[bi][bj] = grid[bi][bj], grid[i][j]

        # 딕셔너리 위치 정보 업데이트
        dct[x] = (bi, bj)
        dct[other] = (i, j)

# 최종 격자 출력
for row in grid:
    print(*row)
