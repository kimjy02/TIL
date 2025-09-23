'''
    동 서 북 남
    1  2 3  4
'''

N, M, x, y, K = map(int, input().split())

map_info = [list(map(int, input().split())) for _ in range(N)]
rotate_direction = list(map(int, input().split()))

# 아래 북 위 남 서 동
dice = [0, 0, 0, 0, 0, 0]
'''
    동쪽 방향으로 회전 : 아래 북 위 남 서 동 -> 서 북 동 남 위 아래
    서쪽 방향으로 회전 : 아래 북 위 남 서 동 -> 동 북 서 남 아래 위
    북쪽 방향으로 회전 : 아래 북 위 남 서 동 -> 남 아래 북 위 서 동 
    남쪽 방향으로 회전 : 아래 북 위 남 서 동 -> 북 위 남 아래 서 동
'''
def rotate_method(rotate_num, x, y):
    if rotate_num == 1:
        if not (0 <= x < N and 0 <= y+1 < M):
            return x, y
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[5], dice[1], dice[4], dice[3], dice[0], dice[2]
        x, y = x, y+1

    elif rotate_num == 2:
        if not (0 <= x < N and 0 <= y-1 < M):
            return x, y
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[1], dice[5], dice[3], dice[2], dice[0]
        x, y = x, y - 1

    elif rotate_num == 3:
        if not (0 <= x-1 < N and 0 <= y < M):
            return x, y
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]
        x, y = x - 1, y

    elif rotate_num == 4:
        if not (0 <= x+1 < N and 0 <= y < M):
            return x, y
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]
        x, y = x + 1, y

    if map_info[x][y] == 0:
        map_info[x][y] = dice[0]
    else:
        dice[0] = map_info[x][y]
        map_info[x][y] = 0
    print(dice[2])
    return x, y

for rotate_num in rotate_direction:
    x, y = rotate_method(rotate_num, x, y)
