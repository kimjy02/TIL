out = set()
path = []

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def dfs(start):
    if len(path) == M :
        out.add(tuple(path))
        return

    need = M - len(path)
    limit = N - need + 1

    for i in range(start, limit):
        path.append(arr[i])
        dfs(i+1)
        path.pop()

dfs(0)

for answer in sorted(out):
    print(*answer)