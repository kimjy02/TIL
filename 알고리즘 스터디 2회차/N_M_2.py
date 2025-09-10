import itertools

N, M = map(int, input().split())

lst = list(range(1, N+1))

print(*(list*(itertools.permutations(lst,M))))

