from collections import deque

N = int(input())
apple_count = int(input())

apple_location = [list(map(int, input().split())) for _ in range(apple_count)]

L = int(input())
direction_change = [list(input().split()) for _ in range(L)]

#   북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

snake = deque([(0, 0)])  
direction_idx = 1        
time = 0
next_change_time, next_dir = direction_change.pop(0)


apples = set((r-1, c-1) for r, c in apple_location)

while True:
    time += 1
    head_r, head_c = snake[-1]
    nr, nc = head_r + dr[direction_idx], head_c + dc[direction_idx]
    
    if not (0 <= nr < N and 0 <= nc < N):
        break

    if (nr, nc) in snake:
        break

    if (nr, nc) in apples:
        apples.remove((nr, nc))   
        snake.append((nr, nc))    
    else:
        snake.append((nr, nc))   
        snake.popleft()          

    if int(next_change_time) == time:
        if next_dir == 'L':
            direction_idx = (direction_idx - 1) % 4
        else:
            direction_idx = (direction_idx + 1) % 4
        
        if direction_change:
            next_change_time, next_dir = direction_change.pop(0)

print(time)
