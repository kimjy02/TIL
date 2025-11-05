def dfs(idx):
    global min_value, tower

    tower += H[idx]
    if tower >= B:
        min_value = min(min_value, tower - B)
        return
    for l in range(idx+1, N):
        dfs(l)
        tower -= H[l]

    return

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    # print(H)
    min_value = 10000000
    for i in range(N):
        tower = 0
        dfs(i)

    print(f'#{tc} {min_value}')

