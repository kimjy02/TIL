from collections import deque
import itertools

N, M = map(int, input().split())
house = [list(map(str, input().strip())) for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

path = deque()
things = []

for i in range(M):
    for j in range(N):
        if house[i][j] == 'S':
            start = [i, j]
        if house[i][j] == 'E':
            end = [i, j]
        if house[i][j] == 'X':
            things.append([i, j])

# print(things)
event = (tuple(itertools.permutations(things)))
min_value2 = 1000000
for kind in event:
    route = [start] + list(kind) + [end]
    answer = 0

    for k in range(len(route)-1):
        min_value = 1000000
        visited = [[False] * N for _ in range(M)]
        line = deque()
        r, c = route[k]
        goal = route[k+1]
        line.append([r, c, 0])
        visited[r][c] = True
        found = False
        while line and not found:
            i, j, time = line.popleft()
            for dr_, dc_ in zip(dr, dc):
                nr = i + dr_
                nc = j + dc_
                if 0 <= nr < M and 0 <= nc < N and house[nr][nc] != '#':
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        if [nr, nc] == goal:
                            answer += time +1
                            found = True
                            break
                        line.append([nr, nc, time+1])
    min_value2 = min(answer, min_value2)

print(min_value2)


# while path:
#     i, j, count = path.pop()
#     visited[i][j] = True
#     for r, c in zip(dr, dc):
#         nr = i + r
#         nc = j + c
#         if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
#             path.append([nr, nc, count + 1])
#             visited[nr][nc] = True
#         if 0 <= nr < M and 0 <= nc < N and house[nr][nc] == 'E':
#             min_value = min(min_value, count)

# print(min_value)



