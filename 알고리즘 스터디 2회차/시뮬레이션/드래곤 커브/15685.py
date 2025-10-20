#     우   상   좌  하
dx = [+1, +0, -1, +0]
dy = [+0, -1, +0, +1]

def repeat(x, y, direction, g):
    nx, ny = x+dx[direction], y+dy[direction]
    grid.add((nx, ny))
    if g == 0:
        return
    if direction == 0:
        nx, ny = nx+dx[1], ny+dy[1]
        grid.add((nx, ny))
        for i in range(2, g+1):
            for j in range(2**(i-2)):
                if j == 2**(i-2)-1:
                    nx, ny = nx+dx[2], ny+dy[2]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[1], ny+dy[1]
                    grid.add((nx, ny))

                    # print(nx, ny)
                else:
                    nx, ny = nx+dx[2], ny+dy[2]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[3], ny+dy[3]
                    grid.add((nx, ny))

                    # print(nx, ny)

    elif direction == 1:
        nx, ny = nx+dx[2], ny+dy[2]
        # print(nx, ny)
        grid.add((nx, ny))
        for i in range(2, g+1):
            for j in range(2**(i-2)):
                if j == 2**(i-2)-1:
                    nx, ny = nx+dx[3], ny+dy[3]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[2], ny+dy[2]
                    grid.add((nx, ny))

                    # print(nx, ny)
                else:
                    nx, ny = nx+dx[3], ny+dy[3]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[0], ny+dy[0]
                    grid.add((nx, ny))

                    # print(nx, ny)

    elif direction == 2:
        nx, ny = nx+dx[3], ny+dy[3]
        grid.add((nx, ny))
        for i in range(2, g+1):
            for j in range(2**(i-2)):
                if j == 2**(i-2)-1:
                    nx, ny = nx+dx[0], ny+dy[0]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[3], ny+dy[3]
                    grid.add((nx, ny))

                    # print(nx, ny)
                else:
                    nx, ny = nx+dx[0], ny+dy[0]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[1], ny+dy[1]
                    grid.add((nx, ny))

                    # print(nx, ny)

    elif direction == 3:
        nx, ny = nx+dx[0], ny+dy[0]
        grid.add((nx, ny))
        for i in range(2, g+1):
            for j in range(2**(i-2)):
                if j == 2**(i-2)-1:
                    nx, ny = nx+dx[1], ny+dy[1]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[0], ny+dy[0]
                    grid.add((nx, ny))

                    # print(nx, ny)
                else:
                    nx, ny = nx+dx[1], ny+dy[1]
                    grid.add((nx, ny))

                    # print(nx, ny)
                    nx, ny = nx+dx[2], ny+dy[2]
                    grid.add((nx, ny))

                    # print(nx, ny)

grid = set()

count = 0
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    grid.add((x, y))
    repeat(x, y, d, g)
    # print(grid)
grid_lst = list(grid)
grid_lst.sort()
# print(grid_lst)
for x, y in grid_lst:
    if (x, y+1) in grid_lst and (x+1, y) in grid_lst and (x+1, y+1) in grid_lst:
        count += 1
        # print(x, y)
    else:
        pass
    
print(count)