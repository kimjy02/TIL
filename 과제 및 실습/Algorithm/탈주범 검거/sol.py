'''
    탈주범 검거
    교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생해 수색에 나섰다.
    탈추범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,
    지하 터널 어디가에서 은신 중인 것으로 추정된다.

    터널끼리 연결이 되어 있는 경우 이동이 가능
    -> 탈추범이 있을 수 있는 위치의 계수를 계산해야 함.

    탈추범은 시간 당 1의 거리를 움직일 수 있음
    지하 터널 : 총 7종류의 터널 구조물로 구성되어 있음
    -----------------------------------------------------
    터널 구조물 타입 |   모양   |            기능
          1       |    +    | 상하좌우에 있는 터널과 연결된다.
          2       |    |    |   상하에 있는 터널이 연결된다.
          3       |    ㅡ   |   좌우에 있는 터널이 연결된다.
          4       |    ㄴ   |  상, 우에 있는 터널이 연결된다.
          5       |    「    | 하, 우에 있는 터널이 연결된다.
          6       |    ㄱ   | 하, 좌에 있는 터널이 연결된다.
          7       |    」    | 상, 좌에 있는 터널이 연결된다.
    -----------------------------------------------------
    지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때
    탈추범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성하라.

    제약 사항
        1. 지하 터널 지도의 세로 크기 : N / 가로 크기 : M (5 이상 50 이하)
        2. 맨홀 뚜껑의 세로 위치 : 0 <= R <= (N-1) / 가로 위치 : 0 <= C <= (M-1)
        3. 탈출 후 소요된 시간 : 1 <= L <= 20
        4. 지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장됨
        5. 맨홀 뚜껑은 항상 터널이 있는 위치에 존재함

    입력
        1. T : 테스트 케이스의 수
        2. N : 지하 터널 지도의 세로 크기
           M : 지하 터널 지도의 가로 크기
           R : 맨홀 뚜껑이 위치한 장소의 세로 위치
           C : 맨홀 뚜껑이 위치한 장소의 가로 위치
           L : 탈출 후 소요된 시간
        3. 지하 터널 지도 정보가 주어짐 (각 줄마다 M개의 숫자가 주어짐)
            - 1~7 : 해당 위치의 터널 구조물 타입
            - 0 : 터널이 없는 장소

    출력
        #{tc} {탈출범이 위치할 수 있는 장소의 개수}
'''
# import sys
# sys.stdin = open('sample_input.txt')

#       상  하  좌  우
dx = [ -1, 1,  0, 0]
dy = [  0, 0, -1, 1]

def direction(R, C):
    global tunnel
    global time
    global visited

    if time < L:
        if tunnel[R][C] == 1:
            for x, y in zip(dx, dy):

                if R >= 0 and R <= (N-1) and C >= 0 and C <= (M-1):
                    print(f'1 x좌표 : {R}, y좌표 : {C}')
                    time += 1
                    visited[R][C] += 1
                    # print(time)
                    direction(R, C)
                    R -= x
                    C -= y
                    time -= 1
                else:
                    return

        elif tunnel[R][C] == 2:
            for x, y in zip(dx[:2], dy[:2]):
                R += x
                C += y
                if R >= 0 and R <= (N - 1) and C >= 0 and C <= (M - 1):
                    print(f'2 x좌표 : {R}, y좌표 : {C}')
                    time += 1
                    visited[R][C] += 1
                    direction(R, C)
                    R -= x
                    C -= y
                    time -= 1
                else:
                    return

        elif tunnel[R][C] == 3:
            for x, y in zip(dx[2:], dy[2:]):
                R += x
                C += y
                if R >= 0 and R <= (N - 1) and C >= 0 and C <= (M - 1):
                    print(f'3 x좌표 : {R}, y좌표 : {C}')
                    time += 1
                    visited[R][C] += 1
                    # print(time)
                    direction(R, C)
                    R -= x
                    C -= y
                    time -= 1
                else:
                    return

        elif tunnel[R][C] == 4:
            for x, y in zip([dx[0], dx[3]], [dy[0], dy[3]]):
                R += x
                C += y
                if R >= 0 and R <= (N - 1) and C >= 0 and C <= (M - 1):
                    print(f'4 x좌표 : {R}, y좌표 : {C}')
                    time += 1
                    visited[R][C] += 1
                    direction(R, C)
                    R -= x
                    C -= y
                    time -= 1
                else:
                    return

        elif tunnel[R][C] == 5:
            for x, y in zip([dx[1], dx[3]], [dy[1], dy[3]]):
                R += x
                C += y
                if R >= 0 and R <= (N - 1) and C >= 0 and C <= (M - 1):
                    print(f'5 x좌표 : {R}, y좌표 : {C}')
                    time += 1
                    visited[R][C] += 1
                    direction(R, C)
                    R -= x
                    C -= y
                    time -= 1
                else:
                    return

        elif tunnel[R][C] == 6:
            for x, y in zip([dx[1], dx[2]], [dy[1], dy[2]]):
                R += x
                C += y
                if R >= 0 and R <= (N - 1) and C >= 0 and C <= (M - 1):
                    print(f'6 x좌표 : {R}, y좌표 : {C}')
                    time += 1
                    visited[R][C] += 1
                    direction(R, C)
                    R -= x
                    C -= y
                    time -= 1
                else:
                    return

        elif tunnel[R][C] == 7:
            for x, y in zip([dx[0], dx[2]], [dy[0], dy[2]]):
                R += x
                C += y
                if R >= 0 and R <= (N - 1) and C >= 0 and C <= (M - 1):
                    print(f'7 x좌표 : {R}, y좌표 : {C}')
                    time += 1
                    visited[R][C] += 1
                    direction(R, C)
                    R -= x
                    C -= y
                    time -= 1
                else:
                    return

        else:
            visited[R][C] -= 1
            return

    elif time == L and tunnel[R][C] == 0:
        visited[R][C] -= 1
        return

    else:
        return


T = int(input()) # 테스트 케이스 수

for tc in range(1, T+1):
    N, M, R, C, L = map(int,input().split())  # 입력 주석 참고
    tunnel = [[0]*M for _ in range(N)]
    for i in range(N) :
        tunnel[i] = list(map(int, input().split()))
    # print(tunnel)
    time = 1
    visited = [[0]*M for _ in range(N)]
    visited[R][C] = 1
    print(tunnel[R][C])
    direction(R, C)
    print(visited)
    count = 0
    # for row in visited:
    #     for col in row:
    #         if col > 0:
    #             count += 1
    # print(count)