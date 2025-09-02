'''
    교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생
    탈주범은 탈츨한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점을 들어갔으며, 지하 터널 어딘가에서 은신 중
    터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수 계산
    탐주범은 시간 당 1의 거리 움직일 수 있음
    지하 터널 총 7종류로 구성되어 있고 다음과 같다.
    1 : 상하좌우
    2 : 상하
    3 : 좌우
    4 : 상우
    5 : 하우
    6 : 하좌
    7 : 상좌

    ex) 세로 5, 가로 6인 지도
        맨홀 뚜껑의 위치가 (2, 1)로 주어질 경우, 세로 2, 가로 1을 의미하며

    [제약사항]
        1. 시간 제한
        2. 5 <= N, M <= 50
        3. 0 <= R <= (N-1) / 0 <= C <= (M-1)
        4. 1 <= L <= 20
        5. 지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장됨
        6. 맨홀 뚜껑은 항상 터널이 있는 위치에 존재

    [입력]
        1. T : 테스트 케이스 수
        2. N : 지하 터널 지도의 세로 크기
           M : 지하 터널 지도의 세로 크기
           R : 맨홀 뚜껑이 위치한 장소의 세로 위치
           C : 맨홀 뚜껑이 위치한 장소의 가로 위치
           L : 탈출 후 소요된 시간
        3. 지하 터널 지도 정보 (N X M)
            - 1 ~ 7 : 위에서 언급한 터널 구조물 타입
            - 0 : 터널이 없는 장소

    [출력]
        - #{tc} {탈주범이 위치할 수 있는 장소의 개수}
'''
import sys
sys.stdin = open('sample_input.txt')

from collections import deque

#     상  하  좌  우
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

structure = {
    1 : [0, 1, 2, 3],
    2 : [0, 1],
    3 : [2, 3],
    4 : [0, 3],
    5 : [1, 3],
    6 : [1, 2],
    7 : [0, 2]
}
reverse_structure = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2
}

def mapping(map_info, R, C, L):
    cnt = 1
    time = 1
    visited = set()
    visited.add((R,C))
    queue = deque()
    queue.append([R, C, time])
    while queue:
        row, col, p_time = queue.popleft()
        # print(f'pop된 값 : [{row}, {col}]')
        for i in structure.get(map_info[row][col]):
            nr = row + dr[i]
            nc = col + dc[i]
            # print(f'추가 좌표 : [{nr}, {nc}]')
            if 0 <= nr <= (N-1) and 0 <= nc <= (M-1) and map_info[nr][nc] !=0 and (nr, nc) not in visited and reverse_structure.get(i) in structure.get(map_info[nr][nc]):
                queue.append([nr, nc, p_time+1])
                if p_time > L-1 : return cnt
                cnt += 1
                visited.add((nr, nc))
                # print(queue, cnt)
            # print(queue,time, cnt)

    return cnt

T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    # print(map_info)
    print(f'#{tc} {mapping(map_info, R, C, L)}')

