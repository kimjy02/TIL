import itertools

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        k = arr.pop(0)
        answers = (tuple(itertools.combinations(arr, 6)))
        for ans in answers:
            print(*ans)
        print()