out = []
path = []

def dfs(start):
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        # print(out)
        return

    need = M - len(path)
    limit = N - need + 1

    for i in range(start, limit + 1):
        path.append(i)
        dfs(i + 1)
        path.pop()

N, M = map(int, input().split())

dfs(1)

print('\n'.join(out))