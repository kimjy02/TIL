def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

A, B = map(int, input().split())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

A_lst.sort()
B_lst.sort()
answer_lst = []

for a in A_lst :
    result = binary_search(B_lst, a, 0, B-1)
    if result is None:
        answer_lst.append(a)
    else:
        pass

print(len(answer_lst))
print(*answer_lst)