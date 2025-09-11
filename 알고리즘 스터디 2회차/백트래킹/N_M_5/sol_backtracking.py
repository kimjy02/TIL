out = []
path = []


def dfs():
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        # print(out)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            dfs()
            path.pop()
            visited[i] = False

N, M = map(int, input().split())

visited = [False]*(N)

arr = list(map(int, input().split()))
arr.sort()

dfs()

print('\n'.join(out))