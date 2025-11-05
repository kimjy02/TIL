def dfs(idx, prob):
    global max_value
    if prob <= max_value:
        return

    if idx == N:
        max_value = max(max_value, prob)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(idx+1, prob*P[idx][i] / 100)
            visited[i] = False
    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    # print(P)
    max_value = 0
    visited = [False] * N
    dfs(0, 1)
    answer = max_value * 100
    print(f'#{tc} {answer:.06f}')

