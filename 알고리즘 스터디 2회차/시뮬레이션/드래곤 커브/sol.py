#     우   상   좌  하
dx = [+1, +0, -1, +0]
dy = [+0, -1, +0, +1]

def draw(x, y, d, g, grid):
    # 1) 방향 시퀀스 만들기
    dirs = [d]
    for _ in range(g):
        for dir_ in reversed(dirs):
            dirs.append((dir_ + 1) % 4)
            print(dirs)

    # 2) 점 찍기
    grid.add((x, y))
    for dir_ in dirs:
        x += dx[dir_]
        y += dy[dir_]
        grid.add((x, y))

N = int(input().strip())
grid = set()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    draw(x, y, d, g, grid)

# 3) 1x1 정사각형 개수 세기 (좌하단 기준 네 꼭짓점 존재 여부)
count = 0
for x in range(100):          # 좌표는 0~100
    for y in range(100):
        if (x, y) in grid and (x+1, y) in grid and (x, y+1) in grid and (x+1, y+1) in grid:
            count += 1
print(count)
