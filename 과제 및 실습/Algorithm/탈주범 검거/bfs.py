'''
    입력
        1. T : 테스트 케이스 수
        2. N : 지하 터널 지도의 세로 크기 (5 <= N <= 50)
           M : 지하 터널 지도의 가로 크기 (5 <= M <= 50)
           R : 맨홀 뚜껑이 위치한 장소의 세로 위치 (0 <= R <= N-1)
           C : 맨홀 뚜껑이 위치한 장소의 가로 위치 (0 <= C <= M-1)
           L : 탈출 후 소요된 시간 (1 <= L <= 20)
        3. 지하 터널 지도 정보
            - 1~7 : 터널 구조물 타입
            - 0 : 터널이 없는 장소

    출력
        - #tc {탈출범이 위치할 수 있는 장소의 개수}
'''
import sys
sys.stdin = open('sample_input.txt')
from collections import deque

#     상   하  좌   우
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

direction = {
    1 : [0, 1, 2, 3],
    2 : [0, 1],
    3 : [2, 3],
    4 : [0, 3],
    5 : [1, 3],
    6 : [1, 2],
    7 : [0, 2]
}

reverse_direction = {
    0 : 1,
    1 : 0,
    2 : 3,
    3 : 2
}

def process(R, C, time):
    visited.add((R,C))
    queue.append([R,C,time])
    position = [0, 0, 0]
    while queue:
        position[0], position[1], position[2] = queue.popleft()
        for i in direction.get(mapping[position[0]][position[1]]):
            nr = position[0] + dr[i]
            nc = position[1] + dc[i]
            if 0 <= nc <= M-1 and 0 <= nr <= N-1:
                if mapping[nr][nc] != 0 and (nr,nc) not in visited and reverse_direction.get(i) in direction.get(mapping[nr][nc]):
                    if position[2] == L:
                        break
                    queue.append([nr,nc,position[2]+1])
                    visited.add((nr,nc))

        # print(position[2], queue)
    return len(visited)




T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    mapping = [list(map(int, input().split())) for _ in range(N)]
    # print(mapping)
    visited = set()
    queue = deque()
    print(f'#{tc} {process(R,C,1)}')