import itertools

N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

answers = sorted(set(itertools.combinations_with_replacement(arr, M)))

for ans in answers:
    print(*ans)