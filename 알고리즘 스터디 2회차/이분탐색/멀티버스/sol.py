# M, N = map(int, input().split())
#
# universe = []
# for _ in range(M):
#     universe.append(list(map(int, input().split())))
#
# # print(*universe)
# unique_universe = []
# for i in range(M):
#     unique_sorted = sorted(set(universe[i]))
#     rank = {v: i for i, v in enumerate(unique_sorted)}
#     print(rank)
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

signatures = []

for _ in range(M):
    universe = list(map(int, input().split()))

    # 1. 좌표 압축
    sorted_unique = sorted(set(universe))
    rank = {v: i for i, v in enumerate(sorted_unique)}

    # 2. 원래 배열에 적용해서 정규화
    compressed = tuple(rank[v] for v in universe)

    # print(compressed)
    signatures.append(compressed)
# print(signatures)
# 3. 같은 패턴(튜플)이 몇 번 나왔는지 세기
from collections import Counter

count = Counter(signatures)
print(count)
# 4. 쌍의 개수 = 조합 공식 nC2 = n*(n-1)//2
answer = sum(c * (c - 1) // 2 for c in count.values())
print(answer)
