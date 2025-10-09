import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))

lo, hi = 1, max(arr)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    # print(f'lo : {lo}, hi : {hi}, mid : {mid}')
    if mid == 0:
        break
    pieces = 0
    for x in arr:
        pieces += x // mid
        # print(f'pieces : {pieces}')
        if pieces >= M:
            break

    if pieces >= M:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
