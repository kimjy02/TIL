from collections import deque

#      동  서  남  북
dr = [+0, +0, +1, -1]
dc = [+1, -1, +0, +0]

process_direction = {
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
}

def search():
    global room_count
    
    path = deque()
    visited = [[False] * N for _ in range(M)]
    
    for i in range(M):
        for j in range(N):
            if visited[i][j] :
                continue

            if not visited[i][j]:
                size = 1
                path.append([i, j])
                visited[i][j] = True

            while path :
                # print(path)
                a, b = path.popleft()
                
                if leading[a][b] == 15:
                    break
                
                for k in process_direction[leading[a][b]]:
                    nr = a + dr[k]
                    nc = b + dc[k]
                    if not visited[nr][nc]:
                        path.append([nr, nc])
                        visited[nr][nc] = True
                        size += 1
                
                print(room_count)
            
            room_count.append(size)
    
    return

    

N, M = map(int, input().split())

leading = [list(map(int, input().split())) for _ in range(M)]
room_count = []
search()

print(len(room_count))
print(max(room_count))



# print(leading)

