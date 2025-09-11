out = []
path = []

def dfs():
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        return

    for i in range(1, N+1):
        path.append(i)
        dfs()
        path.pop()

N, M = map(int, input().split())

arr = list(range(1, N+1))

dfs()

print('\n'.join(out))