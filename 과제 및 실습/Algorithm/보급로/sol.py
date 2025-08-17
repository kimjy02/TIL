'''
    보급로 문제

    배경 : 2차 세계 대전에서 연합군과 독일군의 전투가 점점 치열해지고 있다.
    도로 곳곳이 파손된 상태
        - 공병대 : 출발지(S)에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 함.
        - 도로가 파여진 깊이에 비례하여 복구 시간이 증가

    출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.

    깊이가 1이라면 복구에 드는 시간은 1이라고 가정한다.
    출발지에서 도착지까지 거리에 대해서는 고려할 필요 X
    출발지와 도착지를 제외한 곳 중 0인 곳은 복구 작업이 불필요한 곳

    입력
        1. T : 테스트 케이스 수
        2. N : 지도의 한 변의 크기
        3. 지도 정보

    출력
        - #{tc} {복구 작업에 드는 시간이 가장 작은 경로의 복구 시간}

'''

import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

#     상   하  좌   우
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

def path():
    INF = 10**9
    dist = [[INF] * N for _ in range(N)]

    dist[0][0] = mapping[0][0]
    heap = []
    heappush(heap, (mapping[0][0], 0, 0))

    while heap:
        cost, r, c = heappop(heap)

        if cost > dist[r][c]:
            continue

        if r == N-1 and c == N-1:
            return cost

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + mapping[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heappush(heap, (new_cost, nr, nc))

    return dist[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mapping = [list(map(int, input())) for _ in range(N)]
    # print(mapping)
    ans = path()
    print(f'#{tc} {ans}')
