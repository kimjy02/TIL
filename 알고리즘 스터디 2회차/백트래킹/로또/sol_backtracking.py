while True:
    out = set()
    path = []

    arr = list(map(int, input().split()))
    N = arr.pop(0)
    arr.sort()
    if N == 0:
        break
    else:

        def dfs(start):
            if len(path) == 6 :
                out.add(tuple(path))
                return

            for i in range(start, N):
                path.append(arr[i])
                dfs(i+1)
                path.pop()

        dfs(0)

        for answer in sorted(out):
            print(*answer)
        print()