out = set()
path = []

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def dfs(start):
    if len(path) == M :
        out.add(tuple(path))
        return

    for i in range(start, N):
        path.append(arr[i])
        dfs(i)
        path.pop()

dfs(0)

for answer in sorted(out):
    print(*answer)