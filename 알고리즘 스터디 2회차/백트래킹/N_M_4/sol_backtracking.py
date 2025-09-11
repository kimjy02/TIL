out = []
path = []

def dfs(start):
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        # print(out)
        return

    for i in range(start, N+1):
        path.append(i)
        dfs(i)
        path.pop()

N, M = map(int, input().split())

arr = list(range(1, N+1))

dfs(1)

print('\n'.join(out))