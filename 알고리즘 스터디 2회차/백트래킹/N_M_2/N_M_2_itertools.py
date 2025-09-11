import itertools

N, M = map(int, input().split())

lst = list(range(1, N+1))

ans = (list(itertools.combinations(lst,M)))

for answer in ans:
    print(*answer)