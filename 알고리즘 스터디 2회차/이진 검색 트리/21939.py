import sys
import heapq

input = sys.stdin.readline

# min-heap: (level, problem)
minh = []
# max-heap: (-level, -problem)
maxh = []
# 현재 유효한 문제 -> 레벨 매핑 (lazy deletion용)
alive = {}

def clean_min():
    # minh의 top이 현재 alive 정보와 불일치하면 버림
    while minh:
        l, p = minh[0]
        if alive.get(p) == l:
            return
        heapq.heappop(minh)

def clean_max():
    # maxh의 top이 현재 alive 정보와 불일치하면 버림
    while maxh:
        nl, np = maxh[0]
        l, p = -nl, -np
        if alive.get(p) == l:
            return
        heapq.heappop(maxh)

N = int(input())
for _ in range(N):
    p, l = map(int, input().split())
    alive[p] = l
    heapq.heappush(minh, (l, p))
    heapq.heappush(maxh, (-l, -p))

M = int(input())
out = []
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'recommend':
        x = int(cmd[1])
        if x == 1:
            clean_max()
            nl, np = maxh[0]
            out.append(str(-np))
        else:
            clean_min()
            l, p = minh[0]
            out.append(str(p))

    elif cmd[0] == 'add':
        p, l = int(cmd[1]), int(cmd[2])
        alive[p] = l
        heapq.heappush(minh, (l, p))
        heapq.heappush(maxh, (-l, -p))

    else:  # solved p
        p = int(cmd[1])
        if p in alive:
            del alive[p]  # 힙에서는 lazy로 제거됨

print('\n'.join(out))
