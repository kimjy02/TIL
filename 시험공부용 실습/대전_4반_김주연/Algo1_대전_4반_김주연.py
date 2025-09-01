'''
    N개의 우주 정거장이 있으며, 각 정거장은 1부터 n까지 번호가 매겨져 있다.
    모든 우주 정거장을 연결하는 최소 비용의 통신 네트워크를 구축하는 것
    모든 우주 정거장 사이에 최소한 하나의 통신 경로가 존재하도록 하면서
    전체 네트워크 구축에 필요한 최소 우주 크레딧을 계산하시오.
    <만약 모든 정거장을 연결하는 것이 불가능하다면 -1를 반환하시오.>

    [입력]
        1. T : 테스트 케이스 수 (1 <= T <= 10)
        2. N : 우주 정거장의 수 / M : 가능한 연결의 수 (1 <= N, M <= 10^4)
        3. X_i Y_i cost_i (1 <= cost_i <= 10^5 / X_i != Y_i)

    [출력]
        - #{tc} {최송 비용}
'''

# import sys
# sys.stdin = open('algo1_sample_in.txt')

import heapq

def prim(adj_list, start_vertex):
    # mst 리스트 생성
    mst = []
    # 방문 확인 visited set 생성
    visited = set()
    # 초기 우주 정거장 번호를 visited set에 추가
    visited.add(start_vertex)
    # 초기 우주 정거장에서 갈 수 있는 우주 정거장과 그 비용을 min_heap에 저장 (가중치 기준으로 정렬하기 위해 가중치 먼저 저장)
    min_heap = [[weight, end_vertex] for end_vertex, weight in adj_list[start_vertex]]
    # print(min_heap)
    # 가중치 기준으로 min_heap 정렬(최소 힙)
    heapq.heapify(min_heap)

    # min_heap에 아무 값도 남지 않을 때까지
    while min_heap:
        # 첫번째 값(최소 힙)을 가중치와 끝 노드 변수에 저장
        weight, end_vertex = heapq.heappop(min_heap)

        # 끝 노드 변수가 visited set에 존재한다면 continue
        if end_vertex in visited : continue

        # 끝 노드 변수(다음으로 갈 우주 정거장 번호)를 visited set에 추가
        visited.add(end_vertex)
        # mst 리스트에 [출발하는 우주 정거장 번호, 도착하는 우주 정거장 번호, 비용(가중치)] 추가
        mst.append([start_vertex, end_vertex, weight])
        # print(mst)

        # 도착한 우주 정거장에서 새롭게 출발해야 하니,
        # 도착한 우주 정거장에서 갈 수 있는 또 다른 우주 정거장 번호와 가중치 값을 min_heap에 추가
        for next, weight in adj_list[end_vertex]:
            # 근데, 위에서 말한 또 다른 우주 정거장에 방문한 기록이 있으면 continue
            if next in visited : continue

            # 아니면 min_heap에 추가
            heapq.heappush(min_heap, [weight, next])

    # print(visited)
    # visisted set의 길이가 N가 다를 경우(즉, 모든 우주 정거장에 방문하지 않을 경우) -1 반환
    if len(visited) != N:
        return -1

    return mst


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(M)]
    adj_list = {v : [] for v in range(1, N+1)}
    for s, e, w in info:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))
    # print(adj_list)
    start_vertex = 1 # 초기 우주 정거장 번호 저장
    result = prim(adj_list, start_vertex)

    # 모든 우주 정거장에 방문하지 않아 result값이 -1이면 그대로 출력
    if result == -1 :
        print(f'#{tc} {result}')

    # 모든 정거장을 방문해 mst를 반환했다면, total 변수에 가중치값을 더해 total 출력
    else :
        total = 0
        for lst in result:
            total += lst[2]
        print(f'#{tc} {total}')