import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A_lst = list(map(int, input().split()))

l = r = 0
cur = 0
ans = 0
while True:
    if cur >= M :
        if cur == M :
            ans += 1
        cur -= A_lst[l]
        l += 1
    else:
        if r == len(A_lst) :
            break
        cur += A_lst[r]
        r += 1

print(ans)