import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(N-2):

    if A[i] > 0: break

    left, right = i+1, N-1
    target = -A[i]

    while left < right:
        s = A[left] + A[right]
        if s == target:
            if A[left] == A[right]:
                cnt = right - left + 1
                ans += cnt * (cnt - 1) // 2
                break
            lc = 1
            while left + 1 < right and A[left] == A[left+1]:
                lc += 1
                left += 1
            rc = 1
            while right - 1 > left and A[right] == A[right-1]:
                rc += 1
                right -= 1
            ans += lc * rc
            left += 1
            right -= 1
        elif s < target:
            left += 1
        else:
            right -= 1

print(ans)