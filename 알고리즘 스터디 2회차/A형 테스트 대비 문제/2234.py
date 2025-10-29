from collections import deque

#      동  서  남  북
dr = [+0, +0, +1, -1]
dc = [+1, -1, +0, +0]

process_direction = {
    0 : [0, 1, 2, 3],
    1 : [0, 2, 3],
    2 : [0, 1, 2],
    3 : [0, 2],
    4 : [1, 2, 3],
    5 : [2, 3],
    6 : [1, 2],
    7 : [2],
    8 : [0, 1, 3],
    9 : [0, 3],
    10 : [0, 1],
    11 : [0],
    12 : [1, 3],
    13 : [3],
    14 : [1],
    15 : []
}

def search():
    global room_count, room_id, room_num
    
    path = deque()
    visited = [[False] * N for _ in range(M)]  # 방 개수 확인용
    room_num = [[-1] * N for _ in range(M)]  # 방 번호 기록용

    room_id = 0
    for i in range(M):
        for j in range(N):
            if visited[i][j] :
                continue

            if not visited[i][j]:
                size = 1
                path.append([i, j])
                visited[i][j] = True
                room_num[i][j] = room_id

            while path :
                # print(path)
                a, b = path.popleft()

                # 방 개수와 가장 큰 방 크기 구하기                
                for k in process_direction[leading[a][b]]:
                    nr = a + dr[k]
                    nc = b + dc[k]
                    if not visited[nr][nc]:
                        path.append([nr, nc])
                        visited[nr][nc] = True
                        room_num[nr][nc] = room_id
                        size += 1
                
                # print(room_count)
            
            room_count.append(size)
            room_id += 1
    
# 벽 하나를 제거했을 때 가장 큰 방의 크기 구하기
def largest_wall_remove():
    global room_num
    max_room_after_break = 0
    for i in range(M):
        for j in range(N):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if 0 <= nr < M and 0 <= nc < N:
                    if room_num[i][j] != room_num[nr][nc] and k not in process_direction[leading[i][j]]:
                        new_size = room_count[room_num[i][j]] + room_count[room_num[nr][nc]]
                        max_room_after_break = max(max_room_after_break, new_size)
    
    return max_room_after_break

N, M = map(int, input().split())

leading = [list(map(int, input().split())) for _ in range(M)]
room_count = []
search()

print(len(room_count))
print(max(room_count))
print(largest_wall_remove())


# print(leading)

