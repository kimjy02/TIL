out = []
path = []

def dfs():
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        return

    for i in range(N):
        path.append(arr[i])
        dfs()
        path.pop()


N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
dfs()

print('\n'.join(out))
