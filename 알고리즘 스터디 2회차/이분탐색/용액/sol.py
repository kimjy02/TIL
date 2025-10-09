import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))

lo, hi = 0, N-1
best_sum = 10**18
best_pair = (solution[lo], solution[hi])

while lo < hi :
    ans = solution[lo] + solution[hi]

    if abs(ans) < abs(best_sum):
        best_sum = ans
        best_pair = (solution[lo], solution[hi])

    if ans == 0:
        # print(solution[lo], solution[hi])
        break
    elif ans > 0:
        hi -= 1
    else :
        lo += 1

print(best_pair[0], best_pair[1])




# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return None


# N, M = map(int, input().split())
# tree = list(map(int, input().split()))
#
# lo, hi = 0, max(tree)
# ans = 0
#
# while lo <= hi:
#     mid = (lo + hi) // 2
#     wood = 0
#
#     for a in tree:
#         if a > mid:
#             wood += a - mid
#
#         if wood >= M:
#             break
#
#     if wood >= M:
#         ans = mid
#         lo = mid + 1
#     else:
#         hi = mid - 1
#
# print(ans)