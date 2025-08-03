# import sys
#
#
# sys.stdin = open("input.txt", 'r')
#
# N = sys.stdin.readline()
from collections import deque



N = int(input())
sum = 0

for i in range(0, N):
    matrix = (list(map(int, input().split())))
    queue = deque()
    for num in matrix:
        if num == 1 or num == 2:
            queue.append(num)
        else:
            pass
    while (queue[0] == 2):
        queue.popleft()
    while (queue[-1] == 1):
        queue.pop()

    i = 0
    cnt = 0

    while i < len(queue) - 1 :
        if (queue[i] == 1 and queue[i+1] == 2) or (queue[i] == 2 and queue[i+1] == 1):
            queue = deque(list(queue)[:i] + list(queue)[i+1:])
            cnt += 1
        else:
            i += 1
            pass
    sum += cnt
    print(f'{queue} {cnt}')

print(sum)

# magnetic()


    # for
    # stack = []
    # for int in list:
    #     if int == 1 or int == 2:
    #         stack.append(int)
    #     else:
    #         pass
    # print(stack)

