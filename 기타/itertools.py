K, N = map(int, input().split())

import itertools

lst = list(range(1, K+1))

values = tuple(itertools.product(lst, repeat = N))

for value in values:
    print(type(value))
