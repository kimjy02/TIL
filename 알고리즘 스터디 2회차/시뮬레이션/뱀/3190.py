from collections import deque

N = int(input())
apple_count = int(input())

apple_location = [list(map(int, input().split())) for _ in range(apple_count)]

L = int(input())

direction_change = [list(map(str, input().split())) for _ in range(L)]

# print(apple_location)
# print(direction_change)

snake= [[0, 0, 0, 1]]
snake_length = [[0, 0]]
#    북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def game():
    i, j, time, now_direct = snake.pop()
    rotate_time, direct = direction.pop(0)
    if time == int(rotate_time):
        if direct == 'L':
            now_direct = (now_direct + 1) % 4

        else:
            now_direct = (now_direct - 1) % 4
    
    for lst in apple_location:
        if i == lst[0] and j == lst[1] :
            
            i = i + dr[now_direct]
            j = j + dc[now_direct]

    for lst in snake_length:
        lst[0] = lst[0] + dr[now_direct]
        lst[1] = lst
    snake.append([i+dr[now_direct], j+dc[now_direct], time+1, length, now_direct])


