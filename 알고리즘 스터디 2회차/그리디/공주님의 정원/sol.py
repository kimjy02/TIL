N = int(input())

flowers = []

for _ in range(N):
    ms, ds, me, de = map(int, input().split())
    start = ms * 100 + ds
    end = me * 100 + de
    flowers.append((start, end))

flowers.sort(key=lambda x: (x[0], -x[1]))

current = 301
final = 1201
i = 0
cnt = 0
n = len(flowers)

while current < final:
    max_end = current

    while i < n and flowers[i][0] <= current:
        if flowers[i][1] > max_end:
            max_end = flowers[i][1]
        i += 1

    if max_end == current:
        print(0)
        break

    cnt += 1
    current = max_end
else:
    print(cnt)