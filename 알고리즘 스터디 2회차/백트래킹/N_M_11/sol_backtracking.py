out = set()
path = []

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def dfs():
    if len(path) == M :
        out.add(tuple(path))
        return

    for i in range(N):
        path.append(arr[i])
        dfs()
        path.pop()

dfs()

for answer in sorted(out):
    print(*answer)