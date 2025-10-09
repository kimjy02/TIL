import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

lo, hi = 0, max(tree)
ans = 0

while lo <= hi:
    mid = (lo + hi) // 2
    wood = 0

    for a in tree:
        if a > mid:
            wood += a - mid

        if wood >= M:
            break

    if wood >= M:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)