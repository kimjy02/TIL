import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


adj_list = {v : [] for v in range(1, N+1)}

T = int(input())


for _ in range(T):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)


# print(adj_list)

visited = [False] * (N+1)
q = deque([1])
visited[1] = True

# bfs
while q :
    cur = q.popleft()
    for nxt in adj_list[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)


print(sum(visited) - 1)

# # dfs
# def dfs(u):
#     visited[u] = True
#     for v in adj_list[u]:
#         if not visited[v]:
#             dfs[v]

# dfs[1]
