import sys
from collections import deque
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    # print(password)
    M = int(input())
    result = deque()
    queue = list(map(str, input().split()))
    for i in range(len(queue)):
        if queue[i] == 'I':
            result.append(queue[i:int(queue[i+2])+i+3])
        if queue[i] == 'D':
            result.append(queue[i: i+3])
        if queue[i] == 'A':
            result.append(queue[i:i+int(queue[i+1])+2])

    # print(result)
    while result:
        string = result.popleft()
        if string[0] == 'I':
            password.insert(int(string[1]), *string[3:])
        if string[0] == 'D':
            del password[int(string[1]):int(string[1])+int(string[2])+1]
        if string[0] == 'A':
            for i in range(2, 2+int(string[1])):
                password.append(string[i])

    print(password[:10])



