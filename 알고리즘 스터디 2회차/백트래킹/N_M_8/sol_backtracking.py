out = []
path = []

def dfs(start):
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        # print(out)
        return

    for i in range(start, N):
        path.append(arr[i])
        dfs(i)
        path.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

dfs(0)

print('\n'.join(out))