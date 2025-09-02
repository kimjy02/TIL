'''
   공병대는 출발지(S)에서 도착지(G)까지 가기 위한 도로 복구 작업을  빠른 시간 내에 수행하려 함
   출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 복구 시간 구하기
   깊이가 1이라면 복구에 드는 시간이 1이라고 가정한다.

    출발지에서 도착지까지 거리에 대해서는 고려X
    출발지와 도착지를 제외한 곳이 0인 것은 복구 작업이 불필요한 곳

    [입력]
        1. T : 테스트 케이스 수
        2. N : 지도의 크기
        3. 2차원 배열 형태의 지도 정보

    [출력]
        - #{tc} {출발지에서 도착지까지 가는 경로 중에 복구 작업에 드는 시간이 가장 작은 경로의 복구 시간}
'''

import sys
sys.stdin = open('input.txt')

import heapq, math

#     상  하  좌  우
dy = [-1, +1, +0, +0]
dx = [+0, +0, -1, +1]

def direction(info):
    p_time = [[math.inf] * N for _ in range(N)]
    # print(p_time)
    min_heap = [[0, 0, 0]] # 출발지 정보 입력(복구 시간, x, y)
    while min_heap:
        time, py, px = heapq.heappop(min_heap)
        if p_time[py][px] > time:
            p_time[py][px] = time
        else: continue
        for y, x in zip(dy, dx):
            cy = py + y
            cx = px + x
            if 0 <= cy <= (N-1) and 0 <= cx <= (N-1) and p_time[cy][cx] > info[cy][cx]+time:
                heapq.heappush(min_heap, [(info[cy][cx])+time, cy, cx])
            else:
                continue
    return p_time[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().strip())) for _ in range(N)]
    # print(info)
    print(f'#{tc} {direction(info)}')
