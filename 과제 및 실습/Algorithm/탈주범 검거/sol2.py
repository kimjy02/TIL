'''
    지하 터널 지도의 세로 크기 : 5 <= N <= 50
    지하 터널 지도의 가로 크기 : 5 <= M <= 50
    맨홀 뚜껑의 세로 위치 : 0 <= R <= N-1
    맨홀 뚜껑의 가로 위치 : 0 <= C <= M-1
    탈출 후 소요된 시간 : 1 <= L <= 20
    지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장됨
    맨홀 뚜껑은 항상 터널이 있는 위치에 존재

    입력
        1. T : 테스트 케이스 수
        2. N : 지하 터널 지도의 세로 크기
           M : 지하 터널 지도의 가로 크기
           R : 맨홀 뚜껑이 위치한 장소의 세로 크기
           C : 맨홀 뚜겅이 위치한 장소의 가로 크기
           L : 탈출 후 소요된 시간
        3. 지하 터널 지도의 정보
            - 1 ~ 7: 해당 위치의 터널 구조물 타입
            - 0 : 터널이 없는 장소

    출력
        - #{tc} {탈주범이 위치할 수 있는 장소의 개수}
'''

import sys
sys.stdin = open('sample_input.txt')

#     상   하  좌   우
dx = [+0, +0, -1, +1]
dy = [-1, +1, +0, +0]

def direction(mapping, r, c, L):
    global path, time

    visited[r][c] = 1
    path.add((r,c))

    if time == L:
        return

    else:
        if mapping[r][c] == 1:
            cx = dx
            cy = dy
            # print(1)
            processing(mapping, r, c, cx, cy)

        if mapping[r][c] == 2:
            cx = [dx[0], dx[1]]
            cy = [dy[0], dy[1]]
            # print(2)
            processing(mapping, r, c, cx, cy)

        if mapping[r][c] == 3:
            cx = [dx[2], dx[3]]
            cy = [dy[2], dy[3]]
            # print(3)
            processing(mapping, r, c, cx, cy)

        if mapping[r][c] == 4:
            cx = [dx[0], dx[3]]
            cy = [dy[0], dy[3]]
            # print(4)
            processing(mapping, r, c, cx, cy)

        if mapping[r][c] == 5:
            cx = [dx[1], dx[3]]
            cy = [dy[1], dy[3]]
            # print(5)
            processing(mapping, r, c, cx, cy)

        if mapping[r][c] == 6:
            cx = [dx[1], dx[2]]
            cy = [dy[1], dy[2]]
            # print(6)
            processing(mapping, r, c, cx, cy)

        if mapping[r][c] == 7:
            cx = [dx[0], dx[2]]
            cy = [dy[0], dy[2]]
            # print(7)
            processing(mapping, r, c, cx, cy)

def processing(mapping, r, c, cx, cy):
    global time

    for i in range(len(cx)):
        nx = r + cy[i]
        ny = c + cx[i]
        # print(nx, ny)
        if 0 <= nx <= N-1 and 0 <= ny <= M-1:
            if mapping[nx][ny] == 0 or visited[nx][ny] == 1:
                pass
            else:
                path.add((nx, ny))
                time += 1
                visited[nx][ny] = 1
                direction(mapping, nx, ny, L)
                time -= 1
        else:
            pass


T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # 주석 참고
    mapping = [list(map(int,input().split())) for _ in range(N)]
    # print(mapping)
    path = set()
    time = 1
    visited = [[0]*M for _ in range(N)]
    direction(mapping, R, C, L)
    # print(path)
    print(len(path))

