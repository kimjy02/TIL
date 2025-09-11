import itertools

N, M = map(int, input().split())

arr = list(map(int,input().split()))
arr.sort()


answers = sorted(set(itertools.product(arr, repeat=M)))

for ans in answers:
    print(*ans)