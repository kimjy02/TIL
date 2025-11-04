n = int(input())
lst = list(input().strip())


def calc(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b

def dfs(idx, current):
    global answer

    if idx >= len(lst) :
        answer = max(answer, current)
        return
    
    if idx < len(lst) :
        op = lst[idx-1]
        next_num = int(lst[idx])
        dfs(idx + 2, calc(current, op, next_num))

    if idx + 2 < len(lst):
        op = lst[idx-1]
        inner = calc(int(lst[idx]), lst[idx+1], int(lst[idx+2]))
        dfs(idx+4, calc(current, op, inner))

answer = -1e9

dfs(2, int(lst[0]))

print(answer)