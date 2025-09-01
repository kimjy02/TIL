'''
    그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하라.
    최소 스패닝 트리 : 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
    입력으로 주어지는 그래프는 하나의 연결 그래프임이 보장됨

    입력
        1. T : 테스트 케이스 수 (1 <= T <= 10)
        2. V : 정점의 개수 / E : 간선의 개수  (1 <= V <= 100,000 / 1 <= E <= 200,000)
        3. A B C : A번 정점과 B번 정점이 가중치인 C인 간선으로 연결되어 있다는 의미 (-1,000,000 <= C <= 1,000,000)

    출력
        - #{tc} {최소 스패닝 트리의 가중치}
'''
import sys
sys.stdin = open('sample_input.txt')
class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (len(v) + 1)
        self.rank = [0] * (len(v) + 1)

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px != py :
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[py] < self.rank[px]:
                self.p[px] = py
            else:
                self.p[py] = px
                self.rank[px] += 1

def mst_Kruskal(vertices, edges):
    mst = []
    info.sort(key = lambda x : x[2])
    # print(info)
    ds = DisjointSet(vertices)
    for i in range(len(vertices)+1):
        ds.make_set(i)
    # print(ds.p)
    for k in info:
        s, e, w = k
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e)
            mst.append(k)
    return mst

import heapq

def prim(vertices, info):
    mst = []
    visited = set()
    start_vertex = vertices[1]

    min_heap = [(w, start_vertex, e) for e, w in adj_list[start_vertex]]
    heapq.heapify(min_heap)
    visited.add(start_vertex)

    while min_heap:
        # print(min_heap)
        weight, start, end = heapq.heappop(min_heap)
        if end in visited : continue

        visited.add(end)
        mst.append((start, end, weight))

        for next, weight in adj_list[end]:
            if next in visited: continue
            heapq.heappush(min_heap, (weight, end, next))
    return mst


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = {v : [] for v in range(1, V+1)}
    info = [list(map(int, input().split())) for _ in range(E)]
    vertices = [v for v in range(1, V+1)]
    adj_list = {v : [] for v in vertices}
    for s, e, w in info:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))
    # mst = mst_Kruskal(vertices, info)
    mst = prim(vertices, info)
    result = sum(map(lambda x: x[2], mst))
    # result = sum(lst[2] for lst in mst)
    print(f'#{tc} {result}')

