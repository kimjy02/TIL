n = int(input())
arr = list(map(int, input().split()))

best = arr[0]
curr = arr[0]
for x in arr[1:]:
    curr = max(x, curr + x)  # 현재 구간을 이어갈지, 새로 시작할지
    best = max(best, curr)

print(best)
