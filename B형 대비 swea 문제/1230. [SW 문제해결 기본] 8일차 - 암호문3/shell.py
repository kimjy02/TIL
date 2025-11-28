def dfs(idx, total):
    global ans
    print(idx, total)

    if total > ans:
        return

    if idx == N :
        if total >= B :
            ans = min(ans, total)
        return

    dfs(idx+1, total+heights[idx])
    dfs(idx + 1, total)

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))

    ans = N * 10000
    dfs(0, 0)
    print(f'#{t} {ans-B}')