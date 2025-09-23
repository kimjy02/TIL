lines = [list(map(str, input().strip())) for _ in range(12)]

from collections import deque

queue = deque()

color_list = ['R', 'G', 'B', 'P', 'Y']

queue.append(lines[11][0], 11, 0)

# 4개 이상 모이면 count += 1
# 여러 그룹이 있다면 동시에 터지고 여러 그룹이 터지더라도 count += 1

while queue:
    value, r, c = queue.popleft()
    if value == '.' and len(set(lines[r])) == 1:
        continue
    else:
        if value == '.':
            pass
        else :

            queue.append(lines[r][c+1], r, c+1)
