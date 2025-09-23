'''
    어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하라.
    그림이라는 것은 1로 연결된 것을 한 그림이라고 정의
    가로나 세로로 연결된 것은 연결된 것이고 대각선으로 연결된 것은 떨어진 그림이다.
    그림의 넓이 : 그림에 포함된 1의 개수

    [입력]
        1. n : 도화지 세로 크기 / m : 도화지 가로 크기
        2. 0과 1로 이루어진 그림의 정보
    
    [출력]
        1. 그림의 개수
        2. 가장 넓은 그림의 크기
'''
from collections import deque

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

queue = deque(info[0][0], 0, 0)
count = 0
image_count = 0
image_width = []
visited = [[False]*m for _ in range(n)]
visited[0][0] = True
while queue:
    value, cr, cc = queue.popleft()
    if value == 1:
        for r, c in zip(dr, dc):
            nr = cr + r
            nc = cc + c
            if 0 <= nr <= 4 and 0 <= nc <= 4 and visited[nr][nc] == False:
                queue.append(info[nr][nc], nr, nc)
                visited[nr][nc] = True
                image_count += 1
    else:
        if image_count != 0:
            image_width.append(image_count)
            image_count = 0
            count += 1


import itertools

itertools.product()