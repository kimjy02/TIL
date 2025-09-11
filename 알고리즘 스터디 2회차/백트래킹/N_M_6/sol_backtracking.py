out = []
path = []

def dfs(start):
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        return

    need = M - len(path)
    limit = N - need + 1

    for i in range(start, limit):
        path.append(arr[i])
        dfs(i + 1)
        path.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
dfs(0)

print('\n'.join(out))