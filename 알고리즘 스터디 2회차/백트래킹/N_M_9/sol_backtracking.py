N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [False] * N
path = []
out = []

def dfs(start):

    if start == M:
        out.append(' '.join(map(str, path)))
        return

    used = set()
    for i in range(N):
        if visited[i]:
            continue
        if arr[i] in used:
            continue
        used.add(arr[i])

        visited[i] = True
        path.append(arr[i])
        dfs(start + 1)
        path.pop()
        visited[i] = False

dfs(0)
print('\n'.join(out))
