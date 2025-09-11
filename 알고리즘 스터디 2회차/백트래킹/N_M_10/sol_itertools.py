import itertools

N, M = map(int, input().split())

arr = list(map(int,input().split()))
arr.sort()


answers = set(itertools.combinations(arr, M))
answers = sorted(answers)

for ans in answers:
    print(*ans)