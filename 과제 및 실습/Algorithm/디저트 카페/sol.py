# import sys
# sys.stdin =open('sample_input (1).txt')

T = int(input())

dx = [-1, -1, +1, +1]
dy = [-1, +1, -1, +1]

def move(row, col):
    for x, y in zip(dx, dy):
        if 0 <= row+x <= N-1 and 0 <= col+y <= N-1:
            row += x
            col += y
            for i in path:
                if mapping[row][col] == i:
                    return
                else:
                    if len(path) != 2 and visited[row][col] == 1:
                        return
                    else:
                        path.append(mapping[row][col])
                        visited[row][col] = 1
                        move(row, col)


for tc in range(1, T+1):
    N = int(input())
    mapping = [list(map(int, input().split())) for _ in range(N)]
    # print(mapping)

    for r in range(N):
        for c in range(N):
            path = []
            visited = [[0]*N for _ in range(N)]
            if (r==0 and c==0) or (r==0 and c==N-1) or (r==N-1 and c==0) or (r==N-1 and c==N-1):
                pass
            else:
                path.append(mapping[r][c])
                visited[r][c] = 1
                move(r,c)
                print(path)
                print(visited)


    # print(len(path))
